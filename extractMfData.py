from selenium import webdriver
from pathlib import Path
import os.path
import time 
import re


mainDir=os.getcwd()
os.chdir('resources')
resourceDir=Path(os.getcwd())

filePath=resourceDir / "link.txt"
file=open(filePath,"r")

#back to main dir
os.chdir(mainDir)

COUNTER =1

#Loading link into a list
links=[]
for line in file:
	links.append(line)
file.close()


for url in links:
    
    #extracting data of Mutual Fund
	browser=webdriver.Chrome()
	browser.get(url)

	SCROLL_PAUSE_TIME = 0.5
	last_height = browser.execute_script("return document.body.scrollHeight")

	while True:
		# Scroll down to bottom
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		# Wait to load page
		time.sleep(SCROLL_PAUSE_TIME)

		# Calculate new scroll height and compare with last scroll height
		new_height = browser.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height
    

	#creating a file name
	splitedName = re.split(r'https://groww.in/mutual-funds/', url)
	fund=splitedName[1]
	name=re.sub("-","",fund)
	name=name+".txt"

	filePath=resourceDir / name

	file1=open(filePath,"w")
	file1.write(browser.page_source)
	file1.close()
	browser.close()		




