from time import sleep
import threading
from pytube import YouTube
import argparse
from tqdm import tqdm
from selenium import webdriver


def remove_quotes(_string_):
	_string_ = _string_.replace('"', '')
	return _string_

def replace_blank_space(_string_):
	_string_ = _string_.replace(' ', '+')
	return _string_

def download_video(video):
	if video == "https://www.youtube.com/None":
		pass
	else:
		try:
			YouTube(video).streams.first().download()
		except:
			pass
		

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
	for ripper in rippers:
		ripper.join()
		pbar.update(1)

def init():
	parser = argparse.ArgumentParser(description="PyDown v1.0")
	parser.add_argument("-t", "--topic", type=str ,help="Enter topic name")
	parser.add_argument("-scrl", "--scroll", type=int, help="Enter max scroll")

	args = parser.parse_args()
	get_vids(args.topic, args.scroll)

if __name__ == "__main__":
	init()