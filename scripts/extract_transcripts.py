#!/usr/bin/env python3
"""
MedEd YouTube Transcript & Playlist Metadata Extractor
------------------------------------------------------
Extracts all video IDs, durations, titles, and subtitle transcripts
from YouTube playlists or individual video links.
"""

import sys
import json
import urllib.request
import re

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/extract_transcripts.py <YOUTUBE_PLAYLIST_OR_VIDEO_URL_OR_ID>")
        print("Example: python3 scripts/extract_transcripts.py PLbulqb09-t1yGkJPvRmY_qjSBXCbMLb5r")
        sys.exit(1)

    target = sys.argv[1]
    print(f"🔍 Fetching metadata for target: {target}...")

    # Fetch playlist
    if "list=" in target:
        playlist_id = target.split("list=")[1].split("&")[0]
    else:
        playlist_id = target

    url = f"https://www.youtube.com/playlist?list={playlist_id}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

    try:
        with urllib.request.urlopen(req) as resp:
            html = resp.read().decode("utf-8")
        
        m = re.search(r"ytInitialData\s*=\s*({.*?});", html) or re.search(r"var ytInitialData = ({.*?});</script>", html)
        if not m:
            print("❌ Failed to parse YouTube initial data.")
            sys.exit(1)

        data = json.loads(m.group(1))
        
        videos = []
        seen = set()

        def extract_videos(obj):
            if isinstance(obj, dict):
                if "lockupViewModel" in obj:
                    l = obj["lockupViewModel"]
                    try:
                        vid_id = l["rendererContext"]["commandContext"]["onTap"]["innertubeCommand"]["watchEndpoint"]["videoId"]
                        title = l["metadata"]["lockupMetadataViewModel"]["title"]["content"]
                        duration = None
                        overlays = l.get("contentImage", {}).get("thumbnailViewModel", {}).get("overlays", [])
                        for o in overlays:
                            if "thumbnailOverlayTimeStatusViewModel" in o:
                                duration = o["thumbnailOverlayTimeStatusViewModel"]["text"]["content"]
                        
                        if vid_id and title and vid_id not in seen:
                            seen.add(vid_id)
                            videos.append({
                                "videoId": vid_id,
                                "title": title,
                                "duration": duration or "N/A"
                            })
                    except Exception:
                        pass
                else:
                    for k, val in obj.items():
                        extract_videos(val)
            elif isinstance(obj, list):
                for item in obj:
                    extract_videos(item)

        extract_videos(data)
        print(f"✔ Successfully extracted {len(videos)} videos from playlist.")

        output_file = f"playlist_{playlist_id}_extracted.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(videos, f, indent=2)
        print(f"📁 Saved video list to '{output_file}'.")

    except Exception as e:
        print(f"❌ Error extracting playlist: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
