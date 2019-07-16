import threading, argparse, requests, sys, os
import urllib.request, urllib.error, socket
from support.colors import c_white, c_green, c_red, c_yellow, c_blue
from time import sleep
from tqdm import tqdm
from pytube import YouTube
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# Function: Clearing screen.. no hate pls. I need quick fixes
def ClrScrn():
	os.system('cls' if os.name == 'nt' else 'clear')

# string replace operations
# replace_type = quotes/space
def string_replace(str, replace_type):
	if replace_type == "quotes":
		str = str.replace('"', '')
		str = str.replace("'", "")
	elif replace_type == "space":
		str = str.replace(' ', '+')
	return str

# download vidos
not_downloaded = []
def download_video(video):
	if video == "https://www.youtube.com/None" or video == "None" or video == " None":
		print(f"{c_red}[Error] >> Video 'None' type! Exiting..")
		exit()
	else:
		try:
			print(f"{c_green}[Downloading] {c_yellow}>> {c_blue}{video}{c_white}")
			YouTube(video).streams.first().download()
		except:
			print(f"{c_red}[-] {video}{c_white}")
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
		print(f"{c_red}[Error] >> Unable to download following videos:")
		# for each in not_downloaded,
		for v in not_downloaded:
			# print url
			print(f"{c_red}{v}{c_white}")
		# reattempt the download
		print("Reattempting.. in single thread mode")
		for v in not_downloaded:
			# download one at a time, then next
			download_video(v)

# generate video links
def get_vids(topic, scrl):
	video_links = [] # store video links in list
	topic = string_replace(topic, "quotes") # remove quotes from topic
	topic = string_replace(topic, "space") # replace blank
	site = f"https://www.youtube.com/results?search_query={topic}" # form the url
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options) # start webdriver
	driver.get(site) # open the url
	exec_string = f"window.scrollTo(0, {scrl})" # make page scroll javascript with what user specified
	sleep(1) # delay 3 seconds
	driver.execute_script(exec_string) # execute the javascript on url page
	sleep(2) # delay 5 seconds

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
	url = string_replace(url, "quotes")
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
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
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
	url = string_replace(url, "quotes")
	download_video(url)

# Function: Read VERSION.txt on GitHub
def git_version():
	response = urllib.request.urlopen("https://raw.githubusercontent.com/ProHackTech/PyTubeDown/master/VERSION.txt")
	for content in response:
		return int(content)

# Function: Read local VERSION.txt file
def my_version():
	version_me = 1
	# read current version
	with open("VERSION.txt", "r") as fversion:
		for line in fversion:
			version_me = line
	version_me = int(version_me)
	return version_me

# Function: To compare GitHub and Local version numbers
def update_check():
	version_me, content = my_version(), git_version()
	# compare versions
	if version_me < content:
		print(f"{c_green}[New Version Available]{c_yellow}There is a new version available!{c_white}\nRun {c_blue}/updater/update.py{c_white} for updating!")
		version_diff = (content - version_me)
		print(f"{c_green}[Running Behind] {c_yellow}>> {c_green}{version_diff} {c_white}versions\n\n")
	elif version_me == content:
		print(f"{c_green}[Running Latest] {c_yellow}>> {c_green}v{c_white}{version_me}\n\n")
	elif version_me > content:
		version_diff = (version_me - content)
		print(f"{c_green}[Running Ahead] {c_yellow}>> {c_green}{version_diff} {c_white}versions\n\n")

# Function: displaying banner & update
def banner():
	ClrScrn()
	print(f''' {c_red}
______    _____     _         ______                    
| ___ \  |_   _|   | |        |  _  \                   
| |_/ /   _| |_   _| |__   ___| | | |_____      ___ __  
|  __/ | | | | | | | '_ \ / _ \ | | / _ \ \ /\ / / '_ \ 
| |  | |_| | | |_| | |_) |  __/ |/ / (_) \ V  V /| | | |
\_|   \__, \_/\__,_|_.__/ \___|___/ \___/ \_/\_/ |_| |_|
       __/ |                                            
      |___/          {c_white}                                   
	''')

	print(f"\n[Version Check]...")
	update_check()

# Function: Initialize
def init():
	# banner
	banner()

	# argument parsing
	parser = argparse.ArgumentParser(description="PyTubeDown")
	parser.add_argument("-t", "--topic", help="Enter topic name", type=str)
	parser.add_argument("-scrl", "--scroll", help="Enter max scroll", type=int)
	parser.add_argument("-upd", "--update", help="Update pytubedown", action="store_true")
	parser.add_argument("-pl", "--playlist", help="Download Playlist", type=str)
	parser.add_argument("-l", "--link", help="Single link download", type=str)
	args = parser.parse_args()

	if args.topic:
		if args.scroll:
			get_vids(args.topic, args.scroll)
		else:
			get_vids(args.topic, 0)
	# update script
	elif args.update:
		update_check()
	# playlist download
	elif args.playlist:
		get_playlist(args.playlist)
	elif args.link:
		get_link(args.link)
	else:
		print(f"{c_red}Please specify something{c_white}")

if __name__ == "__main__":
	init()
