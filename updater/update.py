import urllib.request,os
from sys import exit
from shutil import copyfile

def update_dir(src):
	dst = "../" + src
	copyfile(src, dst)
	os.remove(src)
	print(f"updated {src}")

def download_file(url,name):
	try:
		urllib.request.urlretrieve(url, name)
	except:
		print(f"Error downloading: {url}")
	update_dir(name)

lines = open('files.txt').readlines()
lineArray = [line.strip().split(' || ') for line in lines]
for x in lineArray:
	download_file(x[0], x[1])