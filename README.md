<h1 align="center">
	<br>
	<img src="https://raw.githubusercontent.com/ProHackTech/PyTubeDown/master/logo.png" alt="PyTubeDown Logo" width="450" height="250">
	<br>
	PyTubeDown
</h1>

<h5 align="center">
	Download YouTube videos & playlists using Python
</h5>

Due to the new YouTube algorithm changes, PyTube is having issues, so please forgive if the script does not work. Many scripts have stopped working. I hope for someone to pirate every video on YouTube, because internet archive does not archive YouTube licensed videos. Once YouTube decides to delete any video under their license (most videos), they may never come back unless archived by someone.

<h3 align="center">
	Youtube made site changes again. Guys, abandon YouTube for good now. They don't want people to even make downloaders for videos. Legitimate API also doesn't allow to download many videos. Some good videos get deleted and banned. They recently banned many instructional hacking videos as well, meanwhile paying good to few good hackers. Idk what this company is up to. It seems shit to me and my peers.
</h3>

## Features
- [x] Multithreaded downloads
- [x] Download playlist
- [x] Download using video URL
- [x] Download using one keyword
- [x] Download using multiple keywords

## Requirements

### System
- Tested on Windows
- Python 3
- Selenium - Firefox gecko driver

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
