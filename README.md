# Atomagical_Plex_Remote_Quality
Automagically sets remote client playback quality

## What does this do how does it work?
Inside the PlexAPI is a flag completely undocumented called forceAutoAdjustQuality
Through testing I found that setting this flag will allow for any client connected to your server to be set to Auto Quality. I now have confirmation from a Plex rep that this flag does infact set Auto Quality https://www.reddit.com/r/PleX/comments/kcebwa/comment/gfqqbds

By using this script you are setting that hidden flag and making sure that your clients aren't stuck on 720p 2Mbps by default.

## How to install:
1. Download python 3.7+
2. Install all packages in requirements file
3. Edit config with your https server URL and token
4. Run the script and boom Auto Quality setting for all clients without touching their settings.
