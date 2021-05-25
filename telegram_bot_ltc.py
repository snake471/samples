#telegram code: 58521
#imports
import os
import time
import pyautogui
pyautogui.FAILSAFE = False
#locations
FULLSCREEN = (854, 98)
LTC_BOT = (275, 108)
VISIT_SITE = (596, 615)
GO_TO_SITE = (618, 463)
CONFIRM = (799, 429)
CLOSE_SITE = (233, 23)
SLEEP_TIME = 34
#open telegram
os.system('telegram-desktop')

#process telegram stuff
#pyautogui.click(FULLSCREEN)
time.sleep(1)
pyautogui.click(LTC_BOT)

x = 0
while x<100:
	time.sleep(4.5)
	pyautogui.click(VISIT_SITE)
	time.sleep(4)
	pyautogui.click(GO_TO_SITE)
	time.sleep(3.5)
	pyautogui.click(CONFIRM)
	time.sleep(3)
	#find captcha
	find = pyautogui.locateOnScreen(r'captcha.png', confidence = 0.79)
	if find is None:
		pass

	else:
		print('spotted')
		time.sleep(.5)
		SLEEP_TIME += 4
		pyautogui.moveTo(555, 338)
		pyautogui.click()

	time.sleep(SLEEP_TIME)
	pyautogui.click(CLOSE_SITE)

