import threading, argparse, requests, httplib2, sys, support.colors, support.errors
from subprocess import Popen
from time import sleep
from tqdm import tqdm
from pytube import YouTube
from selenium import webdriver

# replace quotes in string
def remove_quotes(_string_):
	_string_=_string_.replace('"','')
	return _string_

# replce blank space in string
def replace_blank_space(_string_):
	_string_=_string_.replace(' ','+')
	return _string_

# download vidos
def download_video(video):
	if video=="https://www.youtube.com/None":
		print(f"{warning}Video 'None' type! Exiting..")
		exit()
	else:
		try:
			YouTube(video).streams.first().download()
		except:
			pass

# generate video links
def get_vids(topic, scrl):
	video_links = [] # store video links in list
	topic = remove_quotes(topic) # remove quotes from topic
	topic = replace_blank_space(topic) # replace blank
	site = f"https://www.youtube.com/results?search_query={topic}" # form the url
	driver = webdriver.Firefox() # start webdriver
	driver.get(site) # open the url
	exec_string = f"window.scrollTo(0, {scrl})" # make page scroll javascript with what user specified
	sleep(3) # delay 3 seconds
	driver.execute_script(exec_string) # execute the javascript on url page
	sleep(5) # delay 5 seconds

	# find video elements
	video_titles = driver.find_elements_by_id("video-title")

	# save links
	for video_title in video_titles:
		lnk = video_title.get_attribute('href')
		formed_link = f"https://www.youtube.com/{lnk}"
		video_links.append(formed_link)
	driver.quit()

	# download videos with multiple threads
	rippers = [threading.Thread(target=download_video, args=(video,)) for video in video_links] # create list of threads with target to download videos
	pbar = tqdm(total=len(rippers)) # initiate progressbar
	for ripper in rippers: # for each thread in list of threads
		ripper.start() # start thread
	for ripper in rippers:
		ripper.join() # add thread to thread pool
		pbar.update(1) # update progress bar

def read_git_version():
	# read version file from github
	hreq = httplib2.Http()
	response_header,content=hreq.request("https://raw.githubusercontent.com/ProHackTech/pytubedown/master/version.me","GET")
	content=content.decode()
	content=int(content)
	return content

def read_my_version():
	version_me = 0
	# read current version
	with open("version.me", "r") as fversion:
		for line in fversion:
			version_me = line
	version_me = int(version_me)
	return version_me

def update_me():
	version_me, content = read_my_version(), read_git_version()
	# compare versions
	if version_me < content:
		print(f"{success} There is a new version available!\nRun /updater/update.py for updating..")
	else:
		print(f"{c_blue}Already Updated!{c_white}")

parser = argparse.ArgumentParser(description="pytubedown: YouTube video downloader in Python")
parser.add_argument("-t", "--topic", help="Enter topic name", type=str)
parser.add_argument("-scrl", "--scroll", help="Enter max scroll", type=int)
parser.add_argument("-upd", "--update", help="Update pytubedown", action="store_true")
args = parser.parse_args()

isNetworkUp = requests.get("https://duckduckgo.com/")

if isNetworkUp.ok == True:
	my_version = read_my_version()
	print(f"\n{c_green} Version: {c_white} {my_version}\n")
	if args.topic:
		if args.scroll:
			get_vids(args.topic, args.scroll)
		else:
			get_vids(args.topic, 0)
	elif args.update:
		update_me()
	else:
		print(f"{error}Please specify something{print_help}")
else:
	print(f"{error}Your internet is not working!{c_white}")