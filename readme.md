# pyYouDown

A small script to download youtube videos based on search terms using selenium. Multithreaded.

It's not clean. Made for personal use because downloading on single thread sucksss


# Usage

**Help**: `python3 down.py -h` or `python3 down.py --help`

**-t/--topic** = Search Query

**-scrl/--scroll** = scroll height for loading more video (minimum 0, maximum 1000000000000000000000000000000000000)

**Single Search Query/Word**: `python3 down.py -t singleWord -scrl 2000`

**Multiple Search Query/Word**: `python3 down.py -t "multiple words here" -scrl 2000`

**Note**: You may feel that the progressbar is stuck, but it's downlaoding using mutiple threads in qued in background. It tends to finish a lot of threads together at once. So it will jump large percentages.