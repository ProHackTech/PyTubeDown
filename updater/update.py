import urllib.request,os
from sys import exit
from shutil import copyfile

def update_dir(src):
	dst = "../" + src
	copyfile(src,dst)
	os.remove(src)
	print(f"updated {src}")

def download_files(url,name):
	try:
		urllib.request.urlretrieve(url, name)
	except:
		print(f"Error downloading: {url}")
	update_dir(name)

with open("files.txt") as f:
	lines = f.readlines()
for line in lines:
	lineArray=line.split(" || ")
	lineArray[0] = lineArray[0].replace("\n","")
	lineArray[1] = lineArray[1].replace("\n","")
	download_files(lineArray[0],lineArray[1])