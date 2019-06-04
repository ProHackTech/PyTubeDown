import threading
import argparse
import requests
import urllib
import httplib2
import sys
from support.colors import c_white, c_green, c_red, c_yellow, c_blue
from support.errors import error, warning, success, print_help
from time import sleep
from tqdm import tqdm
from pytube import YouTube
from selenium import webdriver

# replace quotes in string
def remove_quotes(_string_):
	_string_=_string_.replace('"', '')
	return _string_

# replce blank space in string
def replace_blank_space(_string_):
	_string_=_string_.replace(' ', '+')
	return _string_

# download vidos
not_downloaded = []
def download_video(video):
	if video == "https://www.youtube.com/None":
		print(f"{warning}Video 'None' type! Exiting..")
		exit()
	else:
		try:
			YouTube(video).streams.first().download()
			print(f"{success} Downloaded: {c_yellow}{video}{c_white}")
		except:
			# try again after timeout
			sleep(3)
			try:
				download_video(video)
			except:
				print(f"{error}[-] {video}{c_white}")
				not_downloaded.append(video)

# thread creator \(~_~)/
def thread_ripper(video_links):
	rippers = [threading.Thread(target=download_video, args=(video,)) for video in video_links] # create list of threads with target to download videos
	pbar = tqdm(total=len(rippers)) # initiate progressbar
	for ripper in rippers: # for each thread in list of threads
		ripper.start() # start thread
	for ripper in rippers:
		ripper.join() # add thread to thread pool
		pbar.update(1) # update progress bar

	sleep(2)

	# try again for not downloaded: multi-theading again
	rippers = [threading.Thread(target=download_video, args=(video,)) for video in not_downloaded] # create list of threads with target to download videos
	pbar = tqdm(total=len(rippers)) # initiate progressbar
	for ripper in rippers: # for each thread in list of threads
		ripper.start() # start thread
	for ripper in rippers:
		ripper.join() # add thread to thread pool
		pbar.update(1) # update progress bar

	# if not_downloaded is not empty
	if len(not_downloaded) > 0:
		# print error message
		print(f"{error}Unable to download following videos:")
		# for each in not_downloaded,
		for v in not_downloaded:
			# print url
			print(f"{c_yellow}{v}{c_white}")
		# reattempt the download
		print("Reattempting.. in single thread mode")
		for v in not_downloaded:
			# download one at a time, then next
			download_video(v)

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
		# get the attributes using selenium
		lnk = video_title.get_attribute('href')
		# concatenation
		formed_link = f"https://www.youtube.com/{lnk}"
		# append formed url to video_links
		video_links.append(formed_link)
	driver.quit()

	# download videos with multiple threads
	thread_ripper(video_links)

def get_playlist(url):
	# remove quoted from the link
	url = remove_quotes(url)
	playlist = "https://www.youtube.com/playlist?list="

	# if the playlist is in watch mode
	# because it's harder to scroll inside that tiny sidenav in YouTube
	if "/watch?v=" in url:
		list_link = url.split("&")[1][5:] # get list unique url
		playlist += list_link # update variable
	else:
		# make playlist same as url
		playlist = url

	# get videos link in playlist
	video_links = []
	# define webdriver
	driver = webdriver.Firefox()
	# get the playlist using selenium
	driver.get(playlist)
	sleep(5) # seconds
	# find elements with class name
	link_elems = driver.find_elements_by_class_name("ytd-playlist-video-renderer")
	print("Gathering videos from playlist..")
	# for each item in link_elems
	for link_elem in link_elems:
		# get the link from href attribute
		watch_link = link_elem.get_attribute('href')
		video_links.append(watch_link) # add new item to the list of video links
	driver.quit() # quit the driver
	# clean video_links of: None
	print("Cleaning video list")
	clean_list = [x for x in video_links if x is not None] # remove the 'None' types from list
	watch_list = [] # define new list
	for item in clean_list: # for each item in clean list
		itemArray = item.split("&") # split the item using '&' character
		watch_list.append(itemArray[0]) # get the first part and add to watch_list
	print(f"Total Videos: {len(watch_list)}") # get the number of items and print
	thread_ripper(watch_list) # start the thread ripper on array

# get get individual links
def get_link(url):
	url = remove_quotes(url)
	download_video(url)

# reading git version of script
def read_git_version():
	# read version file from github
	hreq = httplib2.Http()
	response_header,content=hreq.request("https://raw.githubusercontent.com/ProHackTech/pytubedown/master/version.me","GET")
	content = content.decode()
	content = int(content)
	return content

# reading local version file
def read_my_version():
	version_me = 0
	# read current version
	with open("version.me", "r") as fversion:
		for line in fversion:
			version_me = line
	version_me = int(version_me)
	return version_me

# check for updates
def update_me():
	version_me, content = read_my_version(), read_git_version()
	# compare versions
	if version_me < content:
		print(f"{success} There is a new version available!\nRun /updater/update.py for updating..")
	else:
		print(f"{c_blue}Already Updated!{c_white}")

def networkIsUp():
	try:
		requests.get("https://duckduckgo.com/")
		return True
	except:
		print(f"{error}Your internet is not working!{c_white}")
		return False

parser = argparse.ArgumentParser(description="pytubedown: YouTube video downloader in Python")
parser.add_argument("-t", "--topic", help="Enter topic name", type=str)
parser.add_argument("-scrl", "--scroll", help="Enter max scroll", type=int)
parser.add_argument("-upd", "--update", help="Update pytubedown", action="store_true")
parser.add_argument("-pl", "--playlist", help="Download Playlist", type=str)
parser.add_argument("-l", "--link", help="Single link download", type=str)
args = parser.parse_args()

# ascii art
print('''
 ____ ___  _ _____  _     ____  _____ ____  ____  _      _     
/  __\\  \\///__ __\\/ \\ /\\/  _ \\/  __//  _ \\/  _ \\/ \\  /|/ \\  /|
|  \\/| \\  /   / \\  | | ||| | //|  \\  | | \\|| / \\|| |  ||| |\\ ||
|  __/ / /    | |  | \\_/|| |_\\|  /_ | |_/|| \\_/|| |/\\||| | \\||
\\_/   /_/     \\_/  \\____/\\____/\\____\\____/\\____/\\_/  \\|\\_/  \\|
                                                               
	''')

if networkIsUp() == True:
	# read version
	my_version = read_my_version()
	print(f"\n{c_green} Version: {c_white} {my_version}\n")
	# update the updater that updates this which we are updating here :v
	try:
		urllib.request.urlretrieve("https://raw.githubusercontent.com/ProHackTech/pytubedown/master/updater/update.py", "updater/update.py")
	except:
		print(f"{error}Unable to retreieve updater!{c_white}\n You can manually download it from:{c_yellow} github.com/ProHackTech/pytubedown/tree/master/updater{c_white}\n\n")
	
	# download via topic
	if args.topic:
		if args.scroll:
			get_vids(args.topic, args.scroll)
		else:
			get_vids(args.topic, 0)
	# update script
	elif args.update:
		update_me()
	# playlist download
	elif args.playlist:
		get_playlist(args.playlist)
	elif args.link:
		get_link(args.link)
	else:
		print(f"{error}Please specify something{print_help}")