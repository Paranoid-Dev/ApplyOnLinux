from selenium import webdriver
import re

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
chrome = webdriver.Chrome(options=options, executable_path='./chromedriver')
ogagent = chrome.execute_script("return navigator.userAgent")
chrome.execute_cdp_cmd("Network.setUserAgentOverride",
	{
		"userAgent": re.sub('\(.*?\)', '(Windows NT 10.0; Win64; x64)', ogagent, 1),
	},
		)
chrome.get("https://applymem.jinhakapply.com/Login")


input("Press 'Enter' key to quit")
chrome.quit()
