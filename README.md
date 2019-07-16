<h1 align="center">
	<br>
	<img src="https://raw.githubusercontent.com/ProHackTech/PyTubeDown/master/logo.png" alt="PyTubeDown Logo" width="450" height="250">
	<br>
	PyTubeDown
</h1>

<h5 align="center">
	Download YouTube videos & playlists using Python
</h5>

## Features
- [x] Multithreaded downloads
- [x] Download playlist
- [x] Download using video URL
- [x] Download using one keyword
- [x] Download using multiple keywords

## Whats New v1007
- [x] Fixed downloading issues
- [x] Headless driver (code optimization)

## Requirements

### System
- Tested on Windows
- Python 3
- Selenium - Firefox gecko driver

## Usage

### Demo Video

<h3 align="center">
	<a href="http://www.youtube.com/watch?feature=player_embedded&v=5t2rEQgqcCM" target="_blank">
		<img src="http://img.youtube.com/vi/5t2rEQgqcCM/0.jpg" alt="DNX Firewall Demo" width="480" height="360" border="10" />
	</a>
</h3>

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
