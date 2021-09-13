from selenium import webdriver
import re

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
chrome = webdriver.Chrome(options=options, executable_path='./chromedriver')
ogagent = chrome.execute_script("return navigator.userAgent")
chrome.execute_cdp_cmd("Network.setUserAgentOverride",
	{
#blocked		"userAgent": re.sub('\(.*?\)', '(Windows NT 10.0; Win64; x64)', ogagent, 1),
		"userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
#works		"userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
	},
		)
chrome.get("https://applymem.jinhakapply.com/Login")


input("Press 'Enter' key to quit")
chrome.quit()
