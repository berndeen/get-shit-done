#!/usr/bin/env python3
"""
YouTube Video Scraper
Extracts metadata, transcript, and details from YouTube videos using yt-dlp.

Usage:
    python3 scripts/youtube-scraper.py <youtube_url> [options]

Options:
    --json          Output as JSON
    --transcript    Also fetch transcript/subtitles
    --output DIR    Save output to directory (default: ./scraped)

Requirements:
    pip install yt-dlp

Examples:
    python3 scripts/youtube-scraper.py https://www.youtube.com/watch?v=w4mu057D7vA
    python3 scripts/youtube-scraper.py https://www.youtube.com/watch?v=w4mu057D7vA --json --transcript
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def check_yt_dlp():
    """Ensure yt-dlp is installed."""
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Error: yt-dlp is not installed. Install it with: pip install yt-dlp")
        sys.exit(1)


def extract_video_id(url):
    """Extract video ID from various YouTube URL formats."""
    patterns = [
        r'(?:v=|/v/|youtu\.be/)([a-zA-Z0-9_-]{11})',
        r'(?:embed/)([a-zA-Z0-9_-]{11})',
        r'(?:shorts/)([a-zA-Z0-9_-]{11})',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def scrape_video(url):
    """Scrape video metadata using yt-dlp."""
    result = subprocess.run(
        ["yt-dlp", "--dump-json", "--no-download", url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Error fetching video data: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    return json.loads(result.stdout)


def fetch_transcript(url):
    """Fetch video transcript/subtitles."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        result = subprocess.run(
            [
                "yt-dlp",
                "--write-auto-sub",
                "--write-sub",
                "--sub-lang", "en",
                "--sub-format", "vtt",
                "--skip-download",
                "-o", os.path.join(tmpdir, "%(id)s"),
                url,
            ],
            capture_output=True,
            text=True,
        )

        # Find the subtitle file
        for f in Path(tmpdir).glob("*.vtt"):
            content = f.read_text()
            # Parse VTT to plain text
            lines = []
            for line in content.split("\n"):
                line = line.strip()
                if not line or line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
                    continue
                if re.match(r'^\d{2}:\d{2}', line) or line.startswith("NOTE"):
                    continue
                if re.match(r'^<\d{2}:\d{2}', line):
                    continue
                # Remove HTML tags
                clean = re.sub(r'<[^>]+>', '', line)
                if clean and clean not in lines[-1:]:
                    lines.append(clean)
            return "\n".join(lines)

    return None


def format_duration(seconds):
    """Format seconds into HH:MM:SS."""
    if not seconds:
        return "Unknown"
    hours, remainder = divmod(int(seconds), 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def format_number(n):
    """Format large numbers with commas."""
    if n is None:
        return "Unknown"
    return f"{n:,}"


def format_date(date_str):
    """Format YYYYMMDD to readable date."""
    if not date_str:
        return "Unknown"
    try:
        dt = datetime.strptime(date_str, "%Y%m%d")
        return dt.strftime("%B %d, %Y")
    except ValueError:
        return date_str


def main():
    parser = argparse.ArgumentParser(description="Scrape YouTube video metadata")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--transcript", action="store_true", help="Also fetch transcript")
    parser.add_argument("--output", default="./scraped", help="Output directory (default: ./scraped)")
    args = parser.parse_args()

    check_yt_dlp()

    video_id = extract_video_id(args.url)
    if not video_id:
        print(f"Error: Could not extract video ID from URL: {args.url}", file=sys.stderr)
        sys.exit(1)

    print(f"Scraping video: {video_id}...", file=sys.stderr)
    data = scrape_video(args.url)

    scraped = {
        "video_id": video_id,
        "title": data.get("title"),
        "channel": data.get("channel"),
        "channel_id": data.get("channel_id"),
        "channel_url": data.get("channel_url"),
        "upload_date": data.get("upload_date"),
        "duration": data.get("duration"),
        "duration_formatted": format_duration(data.get("duration")),
        "view_count": data.get("view_count"),
        "like_count": data.get("like_count"),
        "comment_count": data.get("comment_count"),
        "description": data.get("description"),
        "categories": data.get("categories", []),
        "tags": data.get("tags", []),
        "thumbnail": data.get("thumbnail"),
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "scraped_at": datetime.now().isoformat(),
    }

    if args.transcript:
        print("Fetching transcript...", file=sys.stderr)
        transcript = fetch_transcript(args.url)
        if transcript:
            scraped["transcript"] = transcript
        else:
            scraped["transcript"] = None
            print("No transcript available.", file=sys.stderr)

    if args.json:
        print(json.dumps(scraped, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"  {scraped['title']}")
        print(f"{'='*60}")
        print(f"  Channel:    {scraped['channel']}")
        print(f"  Uploaded:   {format_date(scraped['upload_date'])}")
        print(f"  Duration:   {scraped['duration_formatted']}")
        print(f"  Views:      {format_number(scraped['view_count'])}")
        print(f"  Likes:      {format_number(scraped['like_count'])}")
        print(f"  Comments:   {format_number(scraped['comment_count'])}")
        print(f"  Categories: {', '.join(scraped['categories'])}")
        if scraped['tags']:
            print(f"  Tags:       {', '.join(scraped['tags'][:15])}")
        print(f"  URL:        {scraped['url']}")
        print(f"{'='*60}")
        print(f"\nDescription:")
        print(f"{scraped['description']}")
        if args.transcript and scraped.get("transcript"):
            print(f"\n{'='*60}")
            print(f"Transcript:")
            print(f"{'='*60}")
            print(scraped["transcript"])

    # Save to file if output dir specified
    if args.output:
        out_dir = Path(args.output)
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / f"{video_id}.json"
        with open(out_file, "w") as f:
            json.dump(scraped, f, indent=2)
        print(f"\nSaved to: {out_file}", file=sys.stderr)


if __name__ == "__main__":
    main()
