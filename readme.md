<h1 align="center">
	<br>
	<img src="https://raw.githubusercontent.com/ProHackTech/PyTubeDown/master/logo.png" alt="PyTubeDown Logo">
	<br>
	PyTubeDown
</h1>

Download YouTube videos & playlists using Python.

## Features
- [+] Multithreaded downloads
- [+] Download using keyword(s) {Search Terms}
- [+] Download playlist

## Requirements

### System
- Windows Operating System
- Python 3
- Selenium

Currently supports Firefox driver

### Packages Used
- threading
- argparse
- requests
- urllib
- httplib2
- sys
- subprocess
- time
- tqdm
- pytube
- selenium

## Usage

### Help Menu
`python3 down.py -h` or `python3 down.py --help`

### Commands

- **-t/--topic** = Download videos using query/topic
- **-scrl/--scroll** = Page scroll height for loading more videos
- **-upd/--update** = Update the script
- **-pl/--playlist** = Download playlist
- **-l/--link** = Download single video

### Examples

**Single video download**: `down.py -l "Video Url Here"`

**One Query/Word**: `down.py -t singleWord -scrl 2000`

**Multiple Search Query/Words**: `down.py -t "Multiple Words Here" -scrl 2000`

**Playlist Download**: `down.py -pl "Playlist Link Here"`

**Update script**: `down.py -upd`

## Contributions
Any code improvements, suggestions, issues and feature improvements are appreciated!
