import urllib.request,threading,os
from sys import exit
from shutil import copyfile

fileUrls,fileNames,threads=[],[],[]

def update_dir():
	source=destination=""
	for filename in fileNames:
		source=filename
		destination="../"+filename
		if exists(filename):
			os.delete(filename)
		copyfile(source, destination)
	# try determining python initials
	get_initials=input("Enter your python command initials [EX: python3/python/py] >> ")
	command=f"{get_initials} ../down.py"
	Popen(command, shell=True)
	sys.exit()

def download_files(fileurl,filename):
	#urllib.request.urlretrieve(fileurl, filename)
	update_dir()

with open("files.txt") as f:
	lines = f.readlines()
for line in lines:
	lineArray=line.split(" || ")
	lineArray[0] = lineArray[0].replace("\n","")
	lineArray[1] = lineArray[1].replace("\n","")
	fileUrls.append(lineArray[0])
	fileNames.append(lineArray[1])
for x in range(0, len(fileUrls)):
	temp_thread=threading.Thread(target=download_files,args=(fileUrls[x],fileNames[x]))
	threads.append(temp_thread)
for thread in threads:
	thread.start()
for thread in threads:
	thread.join()