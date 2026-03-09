# Close CRM — Tägliche Anruf-Transkript-Analyse

## Entwicklungsplan für n8n-Automatisierung

---

## Überblick

Automatisierter täglicher Workflow, der Anruf-Transkripte aus Close CRM extrahiert, nach Vertriebsmitarbeiter gruppiert und per KI ermittelt, warum Leads nicht qualifiziert sind. Die Ergebnisse werden in ein Google Sheet geschrieben.

**Auslöser:** Täglich um 17:00 Uhr MEZ/MESZ
**Stack:** n8n (Orchestrierung) + Close API (Daten) + Claude API (Analyse)
**Ausgabe:** Google Sheet — eine Zeile pro nicht-qualifiziertem Anruf, gruppiert nach Mitarbeiter

---

## Architektur

```
[Cron-Trigger 17:00 MEZ]
        │
        ▼
[Close API: Mitarbeiter abrufen]
        │
        ▼
[Close API: Heutige Anrufe pro Mitarbeiter]
        │
        ▼
[Filter: Nur Anrufe mit Transkript]
        │
        ▼
[Close API: Lead-Name pro Anruf]
        │
        ▼
[Transkripte pro Mitarbeiter bündeln]
        │
        ▼
[Claude API: Warum ist dieser Lead nicht qualifiziert?]
        │
        ▼
[Zeilen in Google Sheet einfügen]
```

---

## Phase 1 — Zugangsdaten & Einrichtung

### 1.1 Close API Key
- Gehe zu **Close → Settings → API Keys**
- Erstelle einen Key, Name: `n8n-transcript-analysis`
- In n8n: HTTP Basic Auth Credential anlegen — API Key als Benutzername, Passwort leer
- **Base URL:** `https://api.close.com/api/v1/`

### 1.2 Claude API Key
- Key holen von **console.anthropic.com**
- In n8n: als Generic Credential speichern oder direkt im HTTP Request Header verwenden
- **Endpoint:** `https://api.anthropic.com/v1/messages`
- **Headers:** `x-api-key: {key}`, `anthropic-version: 2023-06-01`

### 1.3 Google Sheets
- Erstelle ein Google Sheet mit dieser Kopfzeile:

```
Datum | Mitarbeiter | Lead-Name | Grund nicht qualifiziert | Zitat vom Lead
```

- In n8n: Google Sheets Credential verbinden (OAuth2)
- Sheet-ID und Tab-Name notieren

---

## Phase 2 — Mitarbeiter abrufen

### n8n Node: HTTP Request

```
GET https://api.close.com/api/v1/user/
```

**Pro Benutzer extrahieren:**
- `id` — um Anrufe zu filtern
- `first_name` + `last_name` — für die Mitarbeiter-Spalte

**Filter:** Inaktive Benutzer oder Nicht-Vertriebs-Rollen bei Bedarf ausschließen.

---

## Phase 3 — Heutige Anrufe pro Mitarbeiter abrufen

### n8n Node: Schleife über Mitarbeiter → HTTP Request

Pro Mitarbeiter:

```
GET https://api.close.com/api/v1/activity/call/
```

**Query-Parameter:**

| Parameter | Wert |
|---|---|
| `user_id` | `{agent.id}` |
| `date_created__gt` | `{heute}T00:00:00+01:00` |
| `date_created__lt` | `{heute}T17:00:00+01:00` |
| `_fields` | `id,user_id,lead_id,duration,recording_transcript,date_created` |
| `_limit` | `100` |

### Paginierung
- Wenn `has_more` gleich `true`, `_skip` um 100 erhöhen und wiederholen
- Alle Ergebnisse pro Mitarbeiter sammeln

### Filter
- Anrufe entfernen, bei denen `recording_transcript` gleich `null` ist

**Wichtig:** `recording_transcript` wird standardmäßig NICHT zurückgegeben — es MUSS in `_fields` aufgelistet werden.

---

## Phase 4 — Lead-Namen abrufen

### n8n Node: HTTP Request (pro eindeutiger lead_id)

```
GET https://api.close.com/api/v1/lead/{lead_id}/?_fields=id,display_name
```

`display_name` an jeden Anruf-Datensatz anhängen. Lead-IDs vorher deduplizieren, um unnötige API-Aufrufe zu vermeiden.

---

## Phase 5 — Claude-Analyse

### 5.1 Transkripte pro Mitarbeiter bündeln

Alle Anrufe mit Transkript in ein Paket pro Mitarbeiter. Das hält die Kosten niedrig (ein API-Aufruf pro Mitarbeiter statt pro Anruf).

### 5.2 HTTP Request an Claude

```json
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 4096,
  "messages": [
    {
      "role": "user",
      "content": "<<PROMPT>>"
    }
  ]
}
```

### 5.3 Prompt

```
Du analysierst Vertriebs-Anruftranskripte für Mitarbeiter {{agent_name}}.

Bestimme für jeden Anruf: Ist dieser Lead qualifiziert oder nicht?

Falls NICHT qualifiziert, liefere:
1. Den Grund — in einfacher Sprache, ein Satz
2. Ein direktes Zitat vom Lead, das zeigt warum er nicht qualifiziert ist

Gib NUR Anrufe aus, bei denen der Lead NICHT qualifiziert ist. Überspringe qualifizierte Leads komplett.

TRANSKRIPTE:

{{#each calls}}
---
Anruf: {{lead_name}}
Dauer: {{duration}} Sekunden

{{#each recording_transcript.utterances}}
[{{speaker_side}}] {{speaker_label}}: {{text}}
{{/each}}
---
{{/each}}

Antworte NUR mit validem JSON, kein anderer Text:
[
  {
    "lead_name": "string",
    "reason": "string — einfache Sprache, ein Satz warum nicht qualifiziert",
    "key_quote": "string — ein direktes Zitat vom Lead"
  }
]

Wenn alle Leads qualifiziert sind, gib ein leeres Array zurück: []
```

### 5.4 Modellwahl
- **Standard:** `claude-sonnet-4-6` — schnell, genau, gutes Preis-Leistungs-Verhältnis
- **Budget-Option:** `claude-haiku-4-5` — ca. 10x günstiger, schafft das trotzdem gut
- **Alternative:** GPT-4o funktioniert auch — der Prompt ist modell-unabhängig

---

## Phase 6 — In Google Sheet schreiben

### n8n Node: Google Sheets — Zeilen anhängen

Claude-JSON-Antwort parsen und eine Zeile pro nicht-qualifiziertem Lead anhängen:

| Datum | Mitarbeiter | Lead-Name | Grund nicht qualifiziert | Zitat vom Lead |
|---|---|---|---|---|
| `{heute}` | `{mitarbeiter_name}` | Aus Claude JSON `lead_name` | Aus Claude JSON `reason` | Aus Claude JSON `key_quote` |

Wenn Claude ein leeres Array zurückgibt (alle qualifiziert), nichts schreiben — oder optional eine Zeile: `{datum} | {mitarbeiter} | — | Alle Leads heute qualifiziert | —`

---

## Phase 7 — Fehlerbehandlung

| Szenario | Lösung |
|---|---|
| **Rate Limiting (Close)** | 60 Req/Min — 1s Pause zwischen Aufrufen pro Mitarbeiter |
| **Rate Limiting (Claude)** | n8n Retry bei Fehler: 3 Versuche, 5s Wartezeit |
| **Keine Anrufe heute** | Mitarbeiter überspringen, keine Zeilen |
| **Keine Transkripte** | Mitarbeiter überspringen, keine Zeilen |
| **50+ Anrufe bei einem Mitarbeiter** | In Batches von 20 Transkripten pro Claude-Request aufteilen, Ergebnisse zusammenführen |
| **Claude gibt ungültiges JSON zurück** | Fehler loggen, einmal wiederholen, im Sheet als "Analyse fehlgeschlagen" markieren |

---

## n8n Workflow — Node-Übersicht

| # | Node-Typ | Name | Zweck |
|---|---|---|---|
| 1 | Cron | `Täglich 17:00 MEZ` | Auslöser |
| 2 | HTTP Request | `Mitarbeiter abrufen` | `GET /user/` |
| 3 | Function | `Aktive Mitarbeiter filtern` | Nicht-Vertrieb entfernen |
| 4 | Split In Batches | `Mitarbeiter-Schleife` | Eine Iteration pro Mitarbeiter |
| 5 | HTTP Request | `Anrufe abrufen` | `GET /activity/call/?user_id=...&_fields=recording_transcript,...` |
| 6 | IF | `Weitere Seiten?` | Paginierungs-Schleife |
| 7 | Function | `Transkript vorhanden?` | Anrufe ohne Transkript entfernen |
| 8 | HTTP Request | `Lead-Name abrufen` | `GET /lead/{id}/?_fields=display_name` |
| 9 | Function | `Claude-Payload bauen` | Transkripte + Lead-Namen zum Prompt zusammenführen |
| 10 | HTTP Request | `Claude-Analyse` | `POST /v1/messages` |
| 11 | Function | `Antwort parsen` | JSON-Array aus Claude extrahieren |
| 12 | Google Sheets | `Zeilen anhängen` | Ergebnisse ins Sheet schreiben |
| 13 | NoOp | `Fehlerbehandlung` | Fehler abfangen und melden |

---

## Konfigurationsvariablen

```
CLOSE_API_KEY=         # Close CRM API Key
CLAUDE_API_KEY=        # Anthropic API Key
TIMEZONE=Europe/Berlin # Oder Europe/Amsterdam, Europe/Paris, etc.
GOOGLE_SHEET_ID=       # Ziel-Spreadsheet-ID
GOOGLE_SHEET_TAB=      # Tab-Name (z.B. "DQ-Analyse")
```

---

## Kostenabschätzung

- Durchschnittliches Transkript: ~500-1500 Tokens
- 20 Anrufe pro Mitarbeiter-Batch: ~10.000-30.000 Input-Tokens
- **Pro Mitarbeiter pro Tag:** ~$0,03-0,10 (Sonnet) oder ~$0,003-0,01 (Haiku)
- 5 Mitarbeiter = ~$0,15-0,50/Tag mit Sonnet

---

## Test-Checkliste

- [ ] Close API Key authentifiziert sich erfolgreich
- [ ] Mitarbeiterliste gibt korrekte Benutzer zurück
- [ ] Anrufe-Endpoint gibt `recording_transcript` zurück, wenn in `_fields` angefordert
- [ ] Paginierung funktioniert bei Mitarbeitern mit 100+ Anrufen
- [ ] Lead-Namen werden korrekt aufgelöst
- [ ] Claude gibt valides JSON in der erwarteten Struktur zurück
- [ ] Leeres Array wird zurückgegeben, wenn alle Leads qualifiziert sind
- [ ] Google Sheet Zeilen erscheinen mit korrekten Spalten
- [ ] Cron löst um 17:00 MEZ aus (Sommerzeit/MESZ-Handling prüfen)
- [ ] Kompletter Durchlauf in ~10 Minuten abgeschlossen
