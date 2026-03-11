# Das Get-Shit-Done Skills-System: Drei Skills, Ein Betriebssystem

## Einleitung: Was ist das Ganze?

Das Get-Shit-Done Skills-System ist ein Betriebssystem fuer KI-Agenten. Es besteht aus drei miteinander verbundenen Skills (Faehigkeiten), die zusammen definieren, wie eine KI denkt, plant, organisiert, baut und testet. Die drei Skills sind:

1. **The Brain** (Das Gehirn) - Die Governance-Schicht: Entscheidet, wie viel Aufwand und Aufsicht eine Aufgabe braucht
2. **Executive Dev Architecture** (Architektur) - Die Organisationsschicht: Definiert wer was macht, wie Systeme zusammenhaengen und wie Fehler behandelt werden
3. **Persistent Ideation Engine** (Die Testmaschine) - Die Implementierungsschicht: Baut und testet Code iterativ bis zur Perfektion

Diese drei Skills bilden zusammen ein vollstaendiges System:

```
The Brain                   -->  GOVERNANCE: Denken, Klassifizieren, Entscheiden, Delegieren
Executive Dev Architecture  -->  ORGANISATION: Topologie, Agenten, Plattformen, Vertraege
Persistent Ideation Engine  -->  IMPLEMENTIERUNG: Bauen, Testen, Iterieren, Ausliefern
```

Das System ist wie ein Unternehmen aufgebaut: Das Gehirn ist der CEO, der entscheidet wie wichtig eine Aufgabe ist. Die Architektur ist das Organigramm und die Unternehmensstruktur. Die Testmaschine ist die Fabrik, die das Produkt baut und prueft.

---

## Skill 1: The Brain - Das Gehirn (Version 4.4)

### Was es ist

The Brain ist die Governance-Schicht - das Entscheidungszentrum. Bevor irgendeine Arbeit beginnt, klassifiziert The Brain jede Aufgabe nach Komplexitaet, Risiko und Auswirkung. Basierend auf dieser Klassifizierung wird bestimmt, wie viel Planung, Analyse und Aufsicht noetig ist.

Man kann es sich vorstellen wie einen Fluglotsen: Nicht jedes Flugzeug braucht die gleiche Aufmerksamkeit. Ein kleiner Privatflieger bei klarem Wetter wird anders behandelt als ein Jumbojet bei Sturm.

### Die drei Modi

The Brain hat drei Betriebsmodi, die jeweils ein unterschiedliches Mass an Governance aktivieren:

#### Quick-Modus (Schnell)
- **Wann:** Die Aufgabe hat nur einen sinnvollen Loesungsweg, und wenn etwas schiefgeht, ist nur der lokale Bereich betroffen (niedriger "Blast Radius")
- **Was passiert:** Einfach machen. Minimale Planung, keine grosse Analyse.
- **Beispiele:** Einen Tippfehler korrigieren, eine einfache Funktion schreiben, ein bekanntes Muster anwenden
- **Tier:** Wird als T3 (Elite Executor) behandelt - praezise Ausfuehrung mit Qualitaetskontrolle

#### Standard-Modus (Mittel)
- **Wann:** Es gibt 2-3 moegliche Loesungswege, oder die Aenderung betrifft andere Teile der Pipeline (mittlerer "Blast Radius")
- **Was passiert:** Kurz nachdenken, Alternativen abwaegen, Checkliste durchgehen, dann umsetzen
- **Beispiele:** Eine neue API-Anbindung bauen, einen Daten-Pipeline-Schritt aendern, eine Bibliothek austauschen
- **Tier:** Wird als T2 (Contextual Specialist) behandelt - versteht den Kontext, kann Verbesserungsvorschlaege machen

#### Strategic-Modus (Strategisch)
- **Wann:** Mehrere grundlegend verschiedene Loesungswege existieren UND die Entscheidung hat systemweite Auswirkungen oder ist schwer rueckgaengig zu machen
- **Was passiert:** Vollstaendige Analyse: SWOT-Analyse, Wettbewerb verschiedener Loesungsvorschlaege, formale Architekturentscheidungen (ADRs), moeglicherweise mehrere KI-Agenten, die gegeneinander Vorschlaege machen
- **Beispiele:** Eine komplett neue Systemarchitektur entwerfen, eine kritische Technologieentscheidung treffen, ein bestehendes System von Grund auf umbauen
- **Tier:** Wird als T1 (Executive) oder T1-Super (Synthesizer) behandelt - volle Entscheidungsgewalt

### Das Klassifizierungsprotokoll

```
Gibt es mehrere sinnvolle Loesungswege?
  NEIN --> Ist der Blast Radius lokal? --> JA  --> QUICK
                                       --> NEIN --> STANDARD
  JA   --> Betrifft es mehrere Domaenen oder das ganze System? --> JA  --> STRATEGIC
                                                                --> NEIN --> Schwer rueckgaengig zu machen? --> JA  --> STRATEGIC
                                                                                                             --> NEIN --> STANDARD
```

Die zentrale Regel: Der hoechste ausgeloeste Modus gewinnt. Wenn auch nur ein Aspekt strategisch ist, wird die ganze Aufgabe strategisch behandelt.

### Das Tier-System (Agenten-Hierarchie)

The Brain definiert vier Stufen von KI-Agenten, die sich nicht in Intelligenz, sondern in Zustaendigkeit und Entscheidungsgewalt unterscheiden:

| Tier | Rolle | Zustaendigkeit | Entscheidungsgewalt |
|------|-------|----------------|---------------------|
| T1-Super | Synthesizer | Alles von T1 + bindende Entscheidungen ueber T1-Outputs | Hoechste (unter dem Menschen) |
| T1 | Executive | Volle Systemarchitektur, SWOT, Wettbewerb | Hoch |
| T2 | Contextual Specialist | Eigene Domaene, Pipeline-Bewusstsein | Mittel - kann zurueckschlagen |
| T3 | Elite Executor | Praezise Ausfuehrung innerhalb eines Vertrags | Begrenzt - aber hoechste Qualitaet |

Wichtig: Jeder Tier ist gleich intelligent. Der Unterschied liegt darin, worauf sie Einfluss nehmen duerfen. Ein T3-Agent ist nicht "duemmer" als ein T1-Agent - er hat einfach einen engeren Fokus.

### Der Systemische Kostentest

Bevor eine Entscheidung getroffen wird, muss sie gegen acht Kostendimensionen geprueft werden:

| Kostendimension | Was sie misst |
|-----------------|---------------|
| Tokens/Credits | Verbrauchte KI-Rechenleistung |
| Zeit | Wanduhrzeit von Start bis Ergebnis |
| Compute | CPU, Speicher, Bandbreite, API-Aufrufe |
| Codezeilen | Wartungsaufwand, Angriffsflaeche |
| Kognitive Last | Wie schwer zu verstehen, aendern oder uebergeben |
| Context Window | Die knappste Ressource bei KI-Agenten |
| Menschliche Eingriffe | Jedes Mal, wenn ein Mensch anfassen, pruefen oder reparieren muss |
| Technische Schuld | Zukuenftige Kosten durch heutige Abkuerzungen |

Die vier Fragen des Kostentests:
1. Was kostet das ueber ALLE Dimensionen, nicht nur die offensichtliche?
2. Gibt es einen Weg, der eine Dimension senkt, ohne eine andere wesentlich zu erhoehen?
3. Erzeugt diese Entscheidung zukuenftige Kosten, die jemand anderes bezahlen muss?
4. Haette ein anderer Tier oder Zustaendigkeitsbereich das gleiche Ergebnis zu geringeren Gesamtkosten erreichen koennen?

### SWOT-Analyse (Nur Strategic-Modus)

Im strategischen Modus ist eine SWOT-Analyse Pflicht - keine Ausnahme. Jeder Vorschlag muss alle vier Bereiche abdecken:

- **Staerken (S):** Was funktioniert gut? Welche bestehenden Entscheidungen, Muster und Architekturen geben Hebelwirkung? Was sollte BEWAHRT werden?
- **Schwaechen (W):** Was ist vage, unvollstaendig oder fragil? Wo wuerde ein feindliches Audit Risse aufdecken? Unbenannte Schwaechen werden zu unvorhergesehenen Fehlern.
- **Chancen (O):** Was ist moeglich aber noch nicht gebaut? Welche Faehigkeiten wuerden den Wert vervielfachen?
- **Bedrohungen (T):** Was geht kaputt, wenn wir blind handeln? Zweitordnungseffekte? Wo versteckt sich Aufblaehung, Duplizierung oder Scope Creep?

Anti-Pattern: Nur Staerken = Marketing. Nur Schwaechen = Verzweiflung. Leere Bedrohungen = naiver Optimismus. Dann ist man noch nicht fertig mit Denken.

### Wettbewerbs-Rat (Council) und Schwarm (Swarm)

Fuer besonders wichtige strategische Entscheidungen kann The Brain mehrere KI-Agenten gleichzeitig einsetzen:

**Council (Ideation Council):** 2-3 T1-Agenten arbeiten am GLEICHEN Problem, unabhaengig voneinander. Jeder macht einen vollstaendigen Vorschlag: Ansatz, Architektur, Workflow, Kostenanalyse und Begruendung. Der T1-Super bewertet alle Vorschlaege und waehlt den besten oder kombiniert die besten Elemente.

**Schwarm (Swarm):** N T1-Agenten arbeiten an VERSCHIEDENEN Facetten eines Problems gleichzeitig. Zum Beispiel: Agent A analysiert die Datenbankarchitektur, Agent B die API-Schicht, Agent C die Sicherheitsaspekte. Danach werden alle Ergebnisse zusammengefuehrt.

| Signal | Verwende... |
|--------|-------------|
| Gleiches Problem, mehrere Ansaetze | Council |
| Problem laesst sich in Facetten zerlegen | Swarm |
| Verschiedene Modell-Perspektiven gefragt | Council |
| Tiefe ueber mehrere Dimensionen gleichzeitig | Swarm |

### Budget-Protokoll

Jede Aufgabe kann ein Budget bekommen - eine Obergrenze fuer den Ressourcenverbrauch:

```
Budget: {Scope} | Obergrenze: {Menge} | Einheit: {Tokens|Schritte|Minuten|API-Aufrufe} | Warnung: 80% | Stopp: 100%
```

- Bei 80%: Warnung loggen, weitermachen mit Monitoring
- Bei 100%: STOPP. Teilergebnisse melden. Eskalation an uebergeordnete Instanz.
- Ein Agent darf sein eigenes Budget NICHT selbst erhoehen.

### Modus-Wechsel (Eskalation)

Waehrend der Arbeit kann der Modus nach oben wechseln, wenn sich herausstellt, dass die Aufgabe komplexer ist als gedacht:

```
QUICK --> STANDARD:  Mehrdeutigkeit entdeckt, Downstream-Auswirkung, Qualitaetsproblem
STANDARD --> STRATEGIC:  Bereichsuebergreifend, nicht rueckgaengig machbar, 2+ fehlgeschlagene Reviews
QUICK --> STRATEGIC:  Systemweiter Blast Radius
```

De-Eskalation ist auch moeglich, braucht aber T1-Genehmigung und schriftliche Begruendung.

### Eiserne Gesetze (Iron Laws)

Diese Regeln sind absolut und duerfen niemals gebrochen werden:

1. Kein Vorschlag ohne Analyse (SWOT im Strategic-Modus, Ideation im Standard-Modus)
2. Keine Auslieferung ohne Test
3. Keine Governance-Umgehung unter Druck - wenn man sie umgehen will, braucht man sie am meisten
4. Governance-Kosten unterliegen selbst dem Systemischen Kostentest
5. Den Buchstaben zu verletzen IST den Geist zu verletzen

### Anti-Rationalisierungs-Verteidigung

The Brain hat eine eingebaute Tabelle gegen typische Ausreden:

| Ausrede | Realitaet |
|---------|-----------|
| "Ist einfach, Quick reicht" | Einfach bedeutet nicht niedriger Blast Radius. Pruefe den Blast Radius. |
| "Ich weiss den richtigen Ansatz" | Nenne 2 verworfene Alternativen, sonst hast du nur geraten. |
| "Strategic dauert zu lang" | Die Kosten, SWOT NICHT zu machen = schlechte Architektur in jeder zukuenftigen Entscheidung. |
| "Tests spaeter = gleiche Ziele" | Tests danach: "Was macht das?" Tests vorher: "Was SOLL das machen?" |
| "Zu einfach zum Testen" | Einfacher Code bricht. 30 Sekunden. |

### Audit und Nachverfolgung

The Brain erzeugt automatisch Audit-Events - eine unveraenderliche Chronik aller Entscheidungen:

- Aufgabenklassifizierung (Modus, Vertrauen, Zeitstempel)
- Moduswechsel (von, nach, Ausloeser)
- Hard-Gate-Begegnungen (bestanden/blockiert)
- Budget-Schwellenwert-Ueberschreitungen
- Circuit-Breaker-Ausloesungen

Diese Events sind append-only: Sie koennen nie geaendert oder geloescht werden. Korrekturen erzeugen einen neuen Event, der auf den urspruenglichen verweist.

### Anwendungsfaelle fuer The Brain

1. **Projektstart:** Jede neue Aufgabe wird zuerst klassifiziert. Das verhindert, dass man bei einfachen Dingen zu viel denkt oder bei wichtigen Dingen zu wenig.
2. **Multi-Agenten-Systeme:** The Brain definiert, welcher Tier welche Teilaufgabe bekommt, mit welchem Kontext und welchem Budget.
3. **Architekturentscheidungen:** Bei strategischen Entscheidungen werden SWOT-Analyse, Wettbewerbs-Rat und ADRs aktiviert.
4. **Ressourcen-Management:** Budget-Protokoll und Kostentest stellen sicher, dass keine Ressource unkontrolliert verbraucht wird.
5. **Qualitaetssicherung der Governance selbst:** Die Anti-Rationalisierungs-Tabellen und eisernen Gesetze verhindern, dass man unter Druck die eigenen Regeln umgeht.

---

## Skill 2: Executive Dev Architecture - Die Architektur (Version 3.2)

### Was es ist

Die Executive Dev Architecture ist der Organisationsplan des gesamten Systems. Waehrend The Brain entscheidet WIE VIEL Governance noetig ist, definiert die Architecture WER WAS MACHT, WIE alles zusammenhaengt und WAS BEI FEHLERN PASSIERT.

Man kann es sich vorstellen wie den Bauplan eines Unternehmens: Organigramm, Stellenbeschreibungen, Kommunikationswege, Eskalationsregeln, Infrastruktur und Sicherheitsvorschriften.

### Modularer Aufbau

Die Architecture ist modular aufgebaut - man liest nur das, was man braucht:

```
STATIC CORE .............. ALLE Tiers lesen (Philosophie, Kosten, Ideation, Anti-Patterns)
T1 EXECUTIVE MODULE ...... Nur T1 (SWOT, Council, Delegation, ADRs, State Machines, Vertraege, Orchestrierung)
T2 SPECIALIST MODULE ..... Nur T2 (Pipeline, Rueckfragen, Scoped Ideation, Checklisten)
T3 EXECUTOR MODULE ....... Nur T3 (I/O Vertraege, Quality Gates, Fehler-Signale)
SHARED INFRASTRUCTURE .... Bei Bedarf nachschlagen (Agenten, Vertraege, Plattformen)
```

Warum? Weil das Context Window (der Arbeitsspeicher der KI) die knappste Ressource ist. Ein T3-Agent braucht keine T1-Informationen - das waere verschwendeter Speicher.

### Die Sechs Ebenen (System Topology)

Jede Komponente im System gehoert zu genau einer von sechs Ebenen:

| Ebene | Funktion | Beispiele |
|-------|----------|-----------|
| 1. Ingestion (Aufnahme) | Daten hereinholen | CSVs, Google Sheets, PDFs, Webhooks, APIs, lokale Dateien |
| 2. Validation (Pruefung) | Daten pruefen BEVOR sie verarbeitet werden | Schema, Typen, Duplikate, Pflichtfelder |
| 3. Processing (Verarbeitung) | Daten transformieren | Mapping, Aggregation, Abgleich, Berechnung, Klassifizierung |
| 4. State (Zustand) | Dauerhafter Speicher | IDs, Snapshots, Hashes, Versionen, Ueberschreibungen |
| 5. Output (Ausgabe) | Ergebnisse liefern | Sheets, CSVs, PDFs, Alerts, Dashboards, Cloud Storage |
| 6. Governance (Steuerung) | Kontrolle und Nachverfolgung | Versionierung, Logs, Zugangskontrolle, Geheimnisse, Eskalation |

### Die Sieben Spezialisten (Agent Catalog)

Das System definiert sieben spezialisierte Agenten, jeder mit einem klar abgegrenzten Zustaendigkeitsbereich:

| Agent | Domaene | Was er macht | Eskalation |
|-------|---------|--------------|------------|
| PythonAutomator | Dateitransformationen | Batch-Verarbeitung, PDF-Generierung, Dateiumwandlungen | --> DataOpsAuditor --> Architekt |
| AppsScriptEngineer | Google-Oekosystem | Sheets-Pipelines, Trigger, Menues, Web Apps | --> DataOpsAuditor --> Architekt |
| APIIntegrator | Schnittstellen | OAuth, REST-APIs, Paginierung, Webhooks, Retry-Logik | --> DataOpsAuditor --> Architekt |
| SQLStrategist | Datenbanken | Query-Design, Aggregation, Warehouse-Schemas | --> DataOpsAuditor --> Architekt |
| FrontEndWorkflowUX | Benutzeroberflaeche | Operator UX, Menues, Dashboards, Genehmigungsworkflows | --> Architekt |
| DataOpsAuditor | Datenkontrolle | Logs, Snapshots, Diffs, Dead-Letter-Queues, Audit-Pakete | --> Architekt |
| EcomOpsAnalyst | E-Commerce | Marktplatz-Attribution, Gebuehrenklassifizierung, Auszahlungsabgleich | --> DataOpsAuditor --> Architekt |

Jeder Agent hat einen formalen Vertrag (Contract):

```
CONTRACT:
  agent: Name
  version: Schema-Version
  accepts: [Eingabe-Schemas mit Typen und Pflichtfeldern]
  produces: [Ausgabe-Schemas mit Typen und Garantien]
  sla: Maximaldauer, Retry-Policy, Timeout-Verhalten
  failure_modes: [Aufgelistete Fehlerarten und was dann passiert]
  escalation: Wer wird benachrichtigt, ab welcher Schwelle
  dependencies: [Andere Agenten oder Services die benoetigt werden]
```

### Formale Vertraege und Datenvertraege

Jede Datenuebertragung zwischen Systemen hat einen formalen Vertrag:

```
Jede Eingabe definiert:
- source_name: Woher kommen die Daten?
- timestamp: Wann wurden sie erstellt?
- schema_version: Welches Schema wird verwendet?
- grain: Auf welcher Ebene? (Pro Zeile, pro Tag, pro Produkt)
- required_columns: Welche Spalten MUESSEN vorhanden sein?
- nullable_fields: Welche Felder duerfen leer sein?
- primary_key: Was identifiziert einen Datensatz eindeutig?
```

Verstoss gegen den Vertrag = sofortiger, lauter Fehler. Niemals stillschweigend schlechte Daten durchlassen.

### Workflow State Machines (Zustandsmaschinen)

Jeder mehrstufige Prozess hat EINE verbindliche Zustandsmaschine:

```
ZUSTAENDE: Eingang --> Validiert --> In Bearbeitung --> Review --> Fertig --> Archiviert
UEBERGAENGE: Jeder Wechsel hat: Ausloeser, Bedingung, Nebeneffekte, Rollback
REGELN:
- Kein impliziter Zustand (wenn es nicht im Zustandsspeicher steht, ist es nicht passiert)
- Fehlgeschlagene Uebergaenge landen in einem Haltezustand, nicht im Nirgendwo
- Zustand ist abfragbar - jeder Agent kann fragen "wo steht X gerade?"
- Menschliche Eingriffe sind ein Zustandsuebergang, kein Hintertuerchen
```

### Orchestrierung (Koordination mehrerer Agenten)

Wenn 3 oder mehr Agenten zusammenarbeiten oder Datenabhaengigkeiten bestehen, gibt es explizite Orchestrierungsregeln:

```
- DAG (gerichteter azyklischer Graph) oder sequentiell - pro Pipeline festlegen
- Jeder Knoten: Agent, Tier, Input-Referenz, Output-Referenz, Timeout, Retry
- Fan-out: Merge-Strategie VORHER definieren, bevor parallele Agenten gestartet werden
- Checkpoints: Zustand an jedem Knoten speichern, damit bei Fehler nicht von Null gestartet wird
- Dead-Letter: Jeder Knoten, der nach Retries immer noch fehlschlaegt, schreibt in eine Dead-Letter-Queue - niemals einfach verwerfen
```

### Umgebungs-Promotion (Environment Promotion)

Code bewegt sich durch drei Umgebungen mit Qualitaets-Gates:

```
Entwicklung (dev) --> Staging --> Produktion (prod)

dev --> staging:
  - Alle Tests bestanden
  - Keine hartcodierten Werte
  - Dependencies gepinnt (feste Versionen)

staging --> prod:
  - Parallel-Lauf-Validierung (altes und neues System gleichzeitig, Ergebnisse vergleichen)
  - Rollback-Plan dokumentiert
  - ADR wenn Architektur geaendert

REGELN:
- Niemals Staging ueberspringen fuer "schnelle Fixes" - so geht Produktion kaputt
- Staging verwendet produktionsaehnliche Daten (bereinigt, aber nicht Spielzeugdaten)
- Geheimnisse sind umgebungsspezifisch - niemals Prod-Geheimnisse nach Dev kopieren
- Rollback wird VOR der Promotion getestet, nicht nach dem Fehler
```

### Incident Response (Vorfallsreaktion)

Wenn Produktion kaputtgeht, gibt es ein klares Protokoll:

| Schweregrad | Beschreibung | Wer reagiert |
|-------------|-------------|--------------|
| SEV1 | Datenverlust, Kundenausfall, finanzieller Schaden | Alle Haende, Mensch fuehrt |
| SEV2 | Eingeschraenkter Service, Pipeline steht, SLA gefaehrdet | T1 fuehrt die Reaktion |
| SEV3 | Nicht-blockierender Bug, Workaround vorhanden | T2 loest, T1 wird informiert |

Reaktionsfluss: Erkennen --> Einordnen --> Eindaemmen --> Beheben --> Verifizieren --> Postmortem

Wichtigste Regel: Zuerst die Blutung stoppen (Containment), DANN die Ursache suchen. Jeder SEV1/SEV2 bekommt ein schuldzuweisungsfreies Postmortem.

### Beobachtbarkeit (Observability)

Drei Saeulen der Beobachtbarkeit - was man nicht sehen kann, kann man nicht reparieren:

| Saeule | Was sie liefert |
|--------|-----------------|
| Logs | Strukturierte JSON-Logs, nach Schwere gestuft (debug/info/warn/error), ueber trace_id korreliert |
| Metriken | Durchsatz, Latenz, Fehlerrate, Queue-Tiefe - als Zaehler, Messwerte und Histogramme |
| Traces | Ende-zu-Ende-Verfolgung von Anfragen ueber Agentengrenzen hinweg |

### Geheimnisse-Lebenszyklus (Secrets Lifecycle)

Geheimnisse (API-Keys, Passwoerter, Tokens) haben einen definierten Lebenszyklus:

```
Erstellung:   Im Secret Manager generiert, niemals im Code oder Chat
Speicherung:  Secret Manager (Produktion), Umgebungsvariablen (Entwicklung) - niemals Klartext-Dateien
Zugriff:      Zur Laufzeit injiziert, auf den Agent/Service beschraenkt, der sie braucht
Rotation:     Geplant oder ausgeloest - jedes Geheimnis hat einen Rotationsplan
Widerruf:     Kompromittiert --> sofort widerrufen --> rotieren --> Zugriffslogs pruefen
Audit:        Wer hat wann auf was zugegriffen - abfragbar

REGELN:
- Keine Geheimnisse in Notebooks, Spreadsheets, Slack oder Email - niemals
- Keine geteilten Geheimnisse zwischen Umgebungen
- Jedes Geheimnis hat einen Besitzer (Mensch) und einen Rotationsplan
```

### Plattform-Entscheidungsmatrix

Welche Plattform fuer welchen Zweck:

| Plattform | Bester Einsatz |
|-----------|----------------|
| Google Colab | Prototyping, Batch-Tests, PDF-Assembly, Ad-hoc-Analyse |
| Apps Script | Sheets-native Workflows, Menues, Genehmigungen, leichte Automatisierung |
| Cloud Run Service | APIs, Webhooks, Control Planes, Agenten |
| Cloud Run Job | Naechtliche Jobs, Backfills, Batch-Abgleiche |
| Secret Manager | Produktions-Geheimnisse, Credential Injection |
| OpenClaw / Open WebUI / Ollama | Local-first, datenschutzsensitiv, selbst gehostet |

### Referenz-Index-Architektur

Statt Wissen im Skill einzubetten, wird ein Index kanonischer Dokumentations-URLs gepflegt. Bei Entscheidungen wird die relevante Dokumentation on-demand geholt. Das haelt den Skill schlank und aktuell.

Beispiele aus dem Index:
- Python-Stil --> PEP 8 (https://peps.python.org/pep-0008/)
- Browser-APIs --> MDN Web APIs
- Chrome Extensions --> Chrome Developer Docs
- PDF-Generierung --> pdf-lib API-Docs
- Shopify --> Shopify API Docs

### Anwendungsfaelle fuer Executive Dev Architecture

1. **Multi-Agenten-Systeme aufsetzen:** Die sieben Spezialagenten mit ihren Vertraegen definieren, wer welche Daten bekommt und wer an wen eskaliert
2. **Daten-Pipelines bauen:** Die sechs Ebenen (Aufnahme bis Governance) als Blaupause fuer jeden Datenfluss
3. **Plattform-Auswahl:** Die Entscheidungsmatrix nutzen, um die richtige Plattform fuer den Anwendungsfall zu waehlen
4. **Produktionsbetrieb:** Incident Response, Umgebungs-Promotion, Geheimnisse-Management und Beobachtbarkeit als fertige Frameworks
5. **Teamkoordination:** RACI-Matrizen und formale Agenten-Vertraege fuer klare Zustaendigkeiten
6. **Architekturentscheidungen dokumentieren:** ADRs (Architecture Decision Records) mit vollstaendiger Kostenanalyse und verworfenen Alternativen

---

## Skill 3: Persistent Ideation Engine - Die Testmaschine (Version 4.1)

### Was es ist

Die Persistent Ideation Engine ist ein ML-aehnlicher Trainingsloop fuer Code. Statt "Code schreiben und hoffen, dass er funktioniert" wird der Agent in eine Schleife geschickt: bauen, testen, analysieren, verbessern, nochmal testen - hunderte Male, autonom, bis das Ergebnis kugelsicher ist.

Die Analogie: Eine KI, die ein Videospiel spielt. Sie probiert jeden Weg, stirbt, lernt daraus, aendert ihre Strategie, spielt hunderte Male - bis sie das Level perfekt beherrscht.

### Die Kernregel

**Der Benutzer ist NIEMALS der Tester.** Jedes Mal, wenn der Benutzer eingreifen muss, ist das ein Designfehler. Das Ziel:

- **DU** fuehrst die Tests durch - hunderte davon
- **DU** findest Bugs, bevor der Benutzer es tut
- **DU** pruefst deinen eigenen Code wie ein feindlicher Nutzer
- **DU** iterierst bis zur Konvergenz, ohne bei jedem Zyklus um Erlaubnis zu fragen
- **DU** kehrst zum Benutzer nur mit ERGEBNISSEN zurueck, nicht mit Fehlern

### Der Trainingsloop

```
+----------------------------------------------------------+
|                                                          |
|   IDEIEREN --> IMPLEMENTIEREN --> TESTEN --> ANALYSIEREN  |
|      ^                                          |        |
|      +------------------------------------------+        |
|                                                          |
|   Fehler jeder Epoche speisen die Ideation der naechsten |
|   Weitermachen bis Konvergenz - nicht bis "10 Durchlaeufe"|
|                                                          |
+----------------------------------------------------------+
```

### Die Epochen im Detail

#### Epoche 0: Erkundung - Mehrere Loesungswege

Bevor ueberhaupt Code geschrieben wird:

1. **Problem definieren.** Eingaben, Ausgaben, Einschraenkungen, Grenzfaelle, Zielumgebungen.
2. **2-4 grundlegend verschiedene Loesungswege generieren.** Nicht beim ersten Einfall bleiben.
   - Verschiedene Algorithmen, Bibliotheken, Architekturen
   - Verschiedene Kompromisse: Geschwindigkeit vs. Speicher, Einfachheit vs. Flexibilitaet
   - Client-seitig vs. Server-seitig, Streaming vs. Batch, synchron vs. asynchron
3. **Jeden Weg bewerten** gegen reale Einschraenkungen
4. **Den vielversprechendsten waehlen.** Alternativen ranken - wenn dieser an eine Wand stoesst, zum naechsten wechseln

#### Epoche 1: Testgeruest zuerst, dann implementieren

1. **Testgeruest VOR dem Produktionscode bauen.**
   - Die ECHTEN Testdateien des Benutzers verwenden - niemals fabricieren wenn echte Daten existieren
   - Jeden Eingabeformat-/Pfad abdecken
   - PASS/FAIL pro Durchlauf mit Kennzahlen ausgeben (Datensatzanzahl, Trefferquoten, Dateigroessen, Ausfuehrungszeit)
   - Headless ausfuehrbar (Node.js, Sandbox - keine manuellen Browser-Klicks)
2. **Die gewaehlte Loesung implementieren.**
3. **Volle Suite laufen lassen.** Baseline: was besteht, was scheitert, welche Fehler erscheinen.

#### Epoche 2+: Die persistente Feedback-Schleife

Jede Epoche kettet sich an die naechste.

**Schritt 1: Fehler UND Erfolge analysieren**
- Fehler: Welche Annahme war falsch? Grenzfall uebersehen? Ist die Korrektur ein Pflaster oder Ursachenbehandlung?
- Erfolge: Unnoetige Arbeit? Redundante Kopien, verschwendete Zuweisungen, wiederholte Berechnungen?

**Schritt 2: Verbesserungen erdenken**
Fuer jeden Befund MEHRERE Loesungen brainstormen:
- Andere Datenstruktur, die den Engpass eliminiert?
- Vorverarbeitungsschritt, der die nachgelagerte Logik vereinfacht?
- Fallback-Pfad fuer graceful Failure statt Absturz?

**Schritt 3: Implementieren und die VOLLE Suite erneut testen**
Nicht nur das, was geaendert wurde. Alles. Jedes Format, jeder Datensatz, jeder Grenzfall. Mindestens 10x pro Testset.

**Schritt 4: Mit vorheriger Epoche vergleichen**
- Hat sich die Bestehensquote verbessert? (Muss >= vorheriger Epoche sein)
- Hat sich die Performance verbessert oder gehalten?
- Ist ein zuvor bestehender Test zurueckgefallen?
- **Bei Regression:** Rueckgaengig machen oder neu denken. Niemals eine Regression ausliefern.

**Schritt 5: In die naechste Epoche verketten**
Analyse dieser Epoche = Input fuer die Ideation der naechsten.

### Praxisbeispiel: Die Verkettung

```
Epoche 2: ArrayBuffer-Detachment beheben --> .slice(0) Kopie
  --> Freigeschaltet: Tests die vorher abstuertzten laufen jetzt
  --> Aufgedeckt: BOM-Doppel-Kodierung in Label Express CSVs (war durch Absturz versteckt)

Epoche 3: BOM-Erkennung reparieren --> Doppelkodierten BOM entfernen
  --> Freigeschaltet: Alle Label Express Tests bestehen
  --> Aufgedeckt: Wortumbruch bei 25 Zeichen laesst Text zu gross erscheinen vs. Referenz

Epoche 4: Referenz-PDF-Spezifikation analysieren --> Umbruch sollte 30 Zeichen sein
  --> Fix, volle Suite nochmal
  --> Aufgedeckt: Zeichenanzahl-Umbruch ist ungenau, Pixel-Breiten-Umbruch ist besser

Epoche 5: Umstellung auf font.widthOfTextAtSize()-Messung
  --> Genauerer Umbruch, symmetrische Raender
  --> 30/30 Tests bestanden, visueller Abgleich bestaetigt --> AUSLIEFERN
```

Jeder Fix hat das naechste Problem aufgedeckt. Das ist die Verkettung.

### Feindliche Selbstpruefung (Adversarial Self-Probing)

Nicht nur den Happy Path testen. Den eigenen Code aktiv kaputt machen:

- **Fehlerhafte Eingaben:** CSVs mit BOM-Kodierung, zusaetzliche Leerzeichen, fehlende Spalten, leere Zeilen
- **Skalierungseingaben:** 200 Seiten statt 5? 500 ITEMDB-Zeilen statt 10?
- **Fehlende Abhaengigkeiten:** Google Sheets Fetch scheitert? Spaltenname leicht anders?
- **Grenzwerte:** Null Elemente, ein Element, maximal lange Namen, Sonderzeichen, Unicode
- **Race Conditions:** Gleiche Operation 10x schnell hintereinander - Zustandsleck zwischen Laeufen?
- **Umgebungsluecken:** Funktioniert in Node.js UND Browser? Funktioniert mit Extension-CSP?

### Progressive Skalierungstests

Schrittweise hochskalieren:

```
Level 1: Kleinster Datensatz (5 Seiten, 5 Datensaetze) x 10 Laeufe
Level 2: Mittlerer Datensatz (15-20 Seiten) x 10 Laeufe
Level 3: Groesster verfuegbarer Datensatz x 10 Laeufe
Level 4: Mehrere Datensaetze im gleichen Lauf (gemischte Formate) x 10 Laeufe
```

Jedes Level kann Probleme aufdecken, die bei kleinerer Skala unsichtbar sind: Speicherwachstum, Performance-Verschlechterung, Index-Ueberlauf.

### Ressourcen-Beschaffung

Bevor der Loop startet, braucht der Agent Testdaten. Die Reihenfolge:

1. **Inventar:** Workspace scannen - Dateien aus frueheren Sessions, Uploads, vorherige Arbeit
2. **Gespraechsverlauf:** URLs, Dateiinhalte, Sheet-IDs, API-Endpunkte, Spaltennamen
3. **Speicher:** Vorherige Sessions, Projektdetails, Dateiorte, Anmeldedaten
4. **Verbundene Dienste:** Google Drive, Notion, Slack, Email

Oft hat man bereits, was man braucht. Nicht nach etwas fragen, was man selbst finden kann.

Falls etwas fehlt: **Einmal fragen, dann selbst loesen.** Synthetische Testdaten generieren, aus Quellcode extrahieren, von URLs abrufen, aus der Ausgabe rueckentwickeln, oder einen Mock bauen. Niemals zweimal nach der gleichen Sache fragen.

### Pfad-Abbruch-Protokoll

Manchmal ist ein Ansatz grundlegend kaputt. Wissen, wann man den Kurs aendern muss:

- **3 aufeinanderfolgende fehlgeschlagene Reparaturversuche** am gleichen Grundproblem: Den Ansatz neu bewerten, nicht nur die Reparatur
- **Umgebungsunmoeglichkeit** (z.B. CORS blockiert API-Aufrufe aus Extension): Zum naechsten gerankten Pfad wechseln
- **Abnehmende Ertraege** (jeder Fix erzeugt neuen Bug): Die Architektur ist falsch, nicht die Implementierung

Wie eine KI, die erkennt, dass eine Strategie das Level niemals schaffen wird, und zu einem komplett anderen Ansatz wechselt.

### Visuelle Ausgabepruefung

Fuer Code, der visuelle Artefakte erzeugt (PDFs, Bilder, Praesentationen):

1. Beispielausgabe aus der Testsuite generieren
2. Rendern und inspizieren - PDF oeffnen, Screenshot machen, jedes Element pruefen
3. Gegen Referenz des Benutzers vergleichen:
   - Schriftgroessen und -gewichte - Quellcode-Spezifikationen pruefen, nicht schaetzen
   - Raender - links UND rechts, symmetrisch wenn Referenz symmetrisch ist
   - Textumbruch - gleiche Umbruchpunkte wie Referenz
   - Layout-Abstaende - messen, nicht raten
4. Abweichung gefunden: Zurueck in den Ideation-Loop

### Anti-Patterns (Was man NICHT tun soll)

| Anti-Pattern | Stattdessen |
|---|---|
| Den Benutzer nach Dateien fragen ohne den Workspace zu pruefen | Workspace, Speicher und Gespraechsverlauf scannen bevor man fragt |
| Zweimal nach der gleichen Sache fragen | Einmal fragen, dann selbst loesen |
| Sich auf den ersten Ansatz festlegen | 2-4 Wege generieren, bewerten, den besten waehlen |
| "Ich habe den Code aktualisiert, probier mal" | Hunderte Tests laufen lassen, dann Ergebnisse liefern |
| Einen Bug fixen ohne alles erneut zu testen | Volle Suite, jedes Format, jedes Mal |
| Nach 10 Durchlaeufen aufhoeren | Weitermachen bis Konvergenz, 10x ist das Minimum |
| Darauf warten, dass der Benutzer Bugs findet | Eigenen Code feindlich pruefen |
| Einen kaputten Ansatz 5+ Mal wiederholen | Den Pfad aufgeben, zum naechsten wechseln |
| "Die Logik sieht korrekt aus" | Denken ist nicht Testen - ausfuehren und verifizieren |

### Anwendungsfaelle fuer die Persistent Ideation Engine

1. **Software-Module bauen:** Browser-Erweiterungen, PDF-Generatoren, Daten-Pipelines, APIs - alles was getestet werden kann
2. **Code portieren:** Python zu JavaScript, Server zu Browser, Colab-Notebook zu Chrome Extension - der Loop faengt alle subtilen Brueche
3. **Unklare Probleme loesen:** Wenn der beste Ansatz nicht offensichtlich ist, probiert die Engine mehrere Wege systematisch durch
4. **Qualitaetssicherung:** Adversarische Selbstpruefung findet Bugs, die ein normaler Test uebersehen wuerde
5. **Visuelle Ausgaben perfektionieren:** PDFs, Berichte, Dashboards - wird gegen Referenz verglichen bis es pixelgenau passt

---

## Wie die drei Skills zusammenarbeiten

### Ablauf bei einer typischen Aufgabe

```
1. BRAIN klassifiziert die Aufgabe
   |
   +--> Quick?    --> Direkt ausfuehren (Ideation Engine im Minimalmodus)
   |
   +--> Standard? --> ARCHITECTURE definiert welcher Agent zustaendig ist
   |                  IDEATION ENGINE baut und testet iterativ
   |
   +--> Strategic? --> ARCHITECTURE definiert Agenten, Vertraege, Orchestrierung
                       BRAIN aktiviert SWOT und/oder Council/Swarm
                       IDEATION ENGINE baut und testet in Epochen
                       BRAIN prueft Ergebnis gegen Kostentest
```

### Verantwortlichkeiten

| Frage | Zustaendiger Skill |
|-------|-------------------|
| Wie wichtig/riskant ist diese Aufgabe? | The Brain |
| Welcher Agent soll das machen? | Executive Dev Architecture |
| Auf welcher Plattform? | Executive Dev Architecture |
| Wie soll der Code getestet werden? | Persistent Ideation Engine |
| Sollen wir mehrere Loesungen vergleichen? | The Brain (Council/Swarm) |
| Was sind die Ein-/Ausgabeformate? | Executive Dev Architecture (Data Contracts) |
| Was passiert bei Fehlern? | Executive Dev Architecture (Failure Model) |
| Wie oft soll getestet werden? | Persistent Ideation Engine (mindestens 10x) |
| Wer muss informiert/gefragt werden? | Executive Dev Architecture (RACI) |
| Duerfen wir in Produktion gehen? | The Brain (Hard Gate) + Architecture (Promotion) |

### Analogie: Das Unternehmen

| Skill | Unternehmensrolle | Tut was |
|-------|-------------------|---------|
| The Brain | CEO + Vorstand | Bewertet jede Aufgabe, entscheidet ueber Governance-Tiefe, verteilt Budgets, verhindert Selbsttaeuschung |
| Executive Dev Architecture | COO + Organigramm + Infrastruktur | Definiert wer was macht, wie kommuniziert wird, welche Plattform fuer was, was bei Fehlern passiert |
| Persistent Ideation Engine | Fabrik + QA-Abteilung | Baut das Produkt, testet es hunderte Male, verbessert es iterativ, liefert erst wenn perfekt |

### Die Philosophie dahinter

Alle drei Skills teilen eine gemeinsame Grundueberzeugung: **Systemisches Denken ueber alle Dimensionen.**

Es geht nie nur um "funktioniert der Code?" sondern immer um die vollstaendige Kostensurface:
- Wie viel KI-Rechenleistung verbraucht es?
- Wie viel menschliche Zeit kostet es?
- Wie wartbar ist es langfristig?
- Wie schwer ist es zu verstehen?
- Welche technische Schuld erzeugt es?
- Wie oft muss ein Mensch eingreifen?

Das System ist darauf ausgelegt, dass die KI-Agenten so autonom wie moeglich arbeiten, mit minimaler menschlicher Intervention, aber mit maximaler Transparenz und Nachverfolgbarkeit.
