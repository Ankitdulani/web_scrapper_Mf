from selenium import webdriver
import time
from pathlib import Path
import os.path

browser = webdriver.Chrome()
url = "https://groww.in/mutual-funds"
browser.get(url) #navigate to the page

SCROLL_PAUSE_TIME = 0.5
scrollNumber=0
# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page

    time.sleep(SCROLL_PAUSE_TIME)
    scrollNumber=scrollNumber+1
    
    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

os.chdir('..')
os.chdir('resources')
location=Path(os.getcwd())
filePath = location / "link.txt"

file=open(filePath,"w")

aTagsInLi = browser.find_elements_by_css_selector('a')
for a in aTagsInLi:
     (file.write( a.get_attribute('href')))
     file.write("\n")

file.close()
browser.close()