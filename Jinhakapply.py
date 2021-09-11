from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
chrome = webdriver.Chrome(options=options, executable_path='./chromedriver')
ogagent = chrome.execute_script("return navigator.userAgent")
chrome.execute_cdp_cmd("Network.setUserAgentOverride",
	{
		"userAgent": ogagent.replace("X11; Linux x86_64", "Windows NT 10.0; Win64; x64"),
	},
		)
chrome.get("https://applymem.jinhakapply.com/Login")


input("Press any key to quit")
chrome.quit()
