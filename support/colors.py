import sys, os, platform

color = True  # Output should be _d
machine = sys.platform  # Detecting the os of current system
checkplatform = platform.platform() # Get current version of OS
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    color = False  # _ shouldn't be displayed in mac & windows
if checkplatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
    color = True
    os.system('') # Enables the ANSI
if not color:
    c_white = c_green = c_red = c_yellow = ''
else:
    c_white = '\033[97m'
    c_green = '\033[92m'
    c_red = '\033[91m'
    c_yellow = '\033[93m'
    c_blue = '\033[94m'