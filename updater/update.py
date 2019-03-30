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

lines = open('files.txt').readlines()
lineArr = [line.split(' || ') for line in lines]
for x in lineArray:
	x.replace('\n','')
	download_file(lineArr[0], lineArr[1])
update_dir(name)