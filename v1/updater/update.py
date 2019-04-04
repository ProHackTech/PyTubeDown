import urllib.request,os
from sys import exit
from shutil import copyfile

# update directories
def update_dir(src):
	dst = "../" + src
	copyfile(src, dst)
	os.remove(src)
	print(f"updated {src}")

# download files
def download_file(url,name):
	try:
		urllib.request.urlretrieve(url, name)
	except:
		print(f"Error downloading: {url}")
	update_dir(name)

# get the file list
try:
	urllib.request.urlretrieve("https://raw.githubusercontent.com/ProHackTech/pytubedown/master/updater/files.txt")
except:
	print(f"Error downloading: {url}")

# read file list
lines = open('files.txt').readlines()
lineArray = [line.strip().split(' || ') for line in lines]
for x in lineArray:
	download_file(x[0], x[1])