import os
import linecache
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import linecache
import time
import pafy
opt = webdriver.ChromeOptions()

browser = webdriver.Chrome('./chromedriver', chrome_options = opt)

x = 0
confirm_links = []
#get videos
browser.get('https://www.youtube.com/')
while x < 251:
	x += 1
	movie = linecache.getline('movs.txt', x)
	search = browser.find_element_by_xpath('//*[@id="search"]')
	search.send_keys(movie)
	time.sleep(1)
	links = browser.find_elements_by_id('video-title')
	check = 0
	i = 1
	while check == 0:
		current = links[i]
		#current.click()
		browser.execute_script('window.scrollTo(0, 100)')
		url = current.get_attribute('href')
		video = pafy.new(url)
		title = video.title
		print(title)
		if 'trailer' in title:
			pass
		
		elif 'soundtrack' or 'SoundTrack' in title:
			pass

		elif 'Official' or 'official' in title:
			pass

		else:
			duration = video.duration
			
			if duration[4:5] < 5 and duration[1:2] < 1:
				check += 2
				browser.get('https://en.savefrom.net')
				input_box = browser.find_element_by_xpath('//*[@id="sf_url"]')
				input_box.send_keys(url)
				start = browser.find_element_by_xpath('//*[@id="sf_submit"]')
				start.click()
				download = browser.find_element_by_xpath('//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a')
				download.click()
				ActionChains(browser).key_down(Keys.LEFT_CONTROL).send_keys('t').key_up(Keys.LEFT_CONTROL).perform()
				browser.get('https://www.youtube.com/')
