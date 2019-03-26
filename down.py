import threading, argparse
from support.colors import *
from support.errors import *
from time import sleep
from tqdm import tqdm
from pytube import YouTube
from selenium import webdriver

# replace quotes in string
def remove_quotes(_string_):
	_string_ = _string_.replace('"', '')
	return _string_

# replce blank space in string
def replace_blank_space(_string_):
	_string_ = _string_.replace(' ', '+')
	return _string_

# download vidos
def download_video(video):
	if video == "https://www.youtube.com/None":
		print(f"{warning}Video 'None' type! Exiting..")
		exit()
	else:
		try:
			YouTube(video).streams.first().download()
		except:
			pass

# generate video links
def get_vids(topic, scrl):
	video_links = []
	topic = remove_quotes(topic)
	topic = replace_blank_space(topic)
	site = f"https://www.youtube.com/results?search_query={topic}"
	driver = webdriver.Firefox()
	driver.get(site)
	exec_string = f"window.scrollTo(0, {scrl})"
	sleep(3)
	driver.execute_script(exec_string) 
	sleep(5)

	# find elements
	video_titles = driver.find_elements_by_id("video-title")

	# save links
	for video_title in video_titles:
		lnk = video_title.get_attribute('href')
		formed_link = f"https://www.youtube.com/{lnk}"
		video_links.append(formed_link)
	driver.quit()

	# download videos
	rippers = [threading.Thread(target=download_video, args=(video,)) for video in video_links]
	pbar = tqdm(total=len(rippers))
	for ripper in rippers:
		ripper.start()
		ripper.join()
		pbar.update(1)

parser = argparse.ArgumentParser(description="PyDown v1.0")
parser.add_argument("-t", "--topic", type=str ,help="Enter topic name")
parser.add_argument("-scrl", "--scroll", type=int, help="Enter max scroll")
args = parser.parse_args()
if args.topic:
	if args.scroll:
		get_vids(args.topic, args.scroll)
	else:
		get_vids(args.topic, 0)
else:
	print(f"{error}Please specify a video topic{print_help}")