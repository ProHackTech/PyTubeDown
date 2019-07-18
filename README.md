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


## License

```

MIT License

Copyright (c) 2019 prohack.tech

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

