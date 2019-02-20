
#making an sinelton class
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


class getHTML:

	#declaring the webbrowser
	browser=None

	def __init__ (self):
		print("module initiated")
		self.initiate()

	def initiate(self):
		print("**** browser instantiated *******")
		self.browser = webdriver.Chrome()

	def getWebPage(self, url):
		self.browser.get(url)

	def getContent(self,url,sleepTime=0):

		self.getWebPage(url)

		SCROLL_PAUSE_TIME = 0.5
		scrollNumber=0
		# Get scroll height
		last_height = self.browser.execute_script("return document.body.scrollHeight")

		while True:
		    # Scroll down to bottom
		    self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		    # Wait to load page

		    time.sleep(SCROLL_PAUSE_TIME)
		    time.sleep(sleepTime)
		    scrollNumber=scrollNumber+1
		    
		    # Calculate new scroll height and compare with last scroll height
		    new_height = self.browser.execute_script("return document.body.scrollHeight")
		    if new_height == last_height:
		        break
		    last_height = new_height

		html=self.browser.page_source

		# self.getNewTab()
		#self.browser.close()
		return (html)

	def getNewTab(self):

		#self.browser.execute_script('''window.open("about:blank", "_blank");''')
		# tabs = (self.browser.get_window_handles());
		# print (tabs)
		curWindowHndl = self.browser.current_window_handle
		self.browser.execute_script('''window.open("about:blank", "_blank");''')
	 	#open link in new tab keyboard shortcut
		time.sleep(0.5) #wait until new tab finishes loading
		newTab=self.browser.window_handles[1]
		self.browser.close() #closes new tab
		self.browser.switch_to_window(newTab)

	def quitBrowser(self):
		print("**** Quiting the Browser ******")
		self.browser.quit()
		