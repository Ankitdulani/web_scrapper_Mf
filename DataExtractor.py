import getHTML
import Beautysoup
import json
import time
from pathlib import Path
import os.path
import re
# work if links.txt not present then work on it


class DataExtractor:

	homePageUrl="https://groww.in/mutual-funds"
	pathResource=os.getcwd()

	def __init__ (self):

		self.context=getHTML.getHTML()
		self.extractor=Beautysoup.Beautysoup()

		currentPath=os.getcwd()
		os.chdir('resources')
		path=Path(os.getcwd())
		os.chdir(currentPath)

		self.pathResource=path


	def extractLinks(self):

		path=self.pathResource / "link.txt"

		flag = (os.path.exists(path))

		if flag == True :
			return self.readFile(path)

		#getscontent From homePage
		htmlPage=self.context.getContent(self.homePageUrl,1)

		#Parse the html document to BeautifulSoup object
		self.extractor.parseHTML(htmlPage)

		#Extract the href attributes value 
		links=self.extractor.findLinks()

		#correcting the link url
		correctedLinks=self.correctLinks(links)

		#writing the file
		self.writeFile("link.txt",correctedLinks)

		#We can write a function to write the link into fileSystem
		return links

	def extractPageContent(self, url):

		print("******** page being extracted ***** ")
		print(url)
		return self.context.getContent(url)

	def extractInformation(self, pageContent):

		self.extractor.parseHTML(pageContent)
		JsonDocument=self.extractor.getInformation()
		return JsonDocument

	def readFile(self, path):
		
		print("******** reading the files ********")
		file=open(path,"r")
		links=[]
		for line in file:
			links.append(line)

		return links

	def writeFile(self , filename , content):

		print("******** writing the files ********")
		path=self.pathResource / filename
		print(path)

		file=open(path,"w")

		for line in content:
		    file.write(line)
		    file.write("\n")

		file.close()

	def handleException(self):
		self.context.quitBrowser()

	def correctLinks(self, links):

		correctedLinks=[]
		print ("****** correcting the links ********** ")
		for link in links:
			link = re.split(r'/n', link)
			link = re.split(r'/mutual-funds',link[0])
			url = self.homePageUrl + str(link[1])
			correctedLinks.append(url)
		return correctedLinks

	def loadDataJSon(self,JsonDocument):

		path=self.pathResource
		path=path / "DATA.json"

		with open(path, 'w') as outfile:
			json.dump(JsonDocument, outfile)

	def newPage(self):
		self.context.getNewTab()

	def reinstantiateBrowser(self):
		self.context.quitBrowser()
		time.sleep(1)
		self.context.initiate()
		time.sleep(2)


def extractInformation(dataExtractor,link,delay):

	pageContent=dataExtractor.extractPageContent(link)
	time.sleep(delay)
	information=dataExtractor.extractInformation(pageContent)
	print(information)
	return information

if __name__ == '__main__':

	dataExtractor=DataExtractor()
	links=dataExtractor.extractLinks()
	
	#Extracting Relevant information from MF
	InformationMF={}
	unprocesssedLinks=[]

	for link in links:

		print("******* Extracting *****")

		# Extraction of Relevant Informqation from the Page 
		# Result into a JSON Format
		# Read Read.me to Understand the model of Information
		try:
			information=extractInformation(dataExtractor,link,3)
			InformationMF[information['name']]=information

		except:
		
			dataExtractor.reinstantiateBrowser();

			try :
				information=extractInformation(dataExtractor,link,5)
				InformationMF[information['name']]=information

			except Exception as ex:

				print ("exception occured")
				print("PAGE NOT LOADED")
				print(ex)
				time.sleep(3)
				unprocesssedLinks.append(link)

		dataExtractor.newPage()


	dataExtractor.writeFile("unprocesssedLinks.txt",unprocesssedLinks)
	dataExtractor.loadDataJSon(InformationMF)
	dataExtractor.handleException()
	
	# except Exception as ex:
	# 	print("exception occured")
	# 	template = "An exception of tpe \" {0} \" occurred. Arguments:\n{1!r}"
	# 	message = template.format(type(ex).__name__, ex.args)
	# 	print (message)
	# 	dataExtractor.handleException()





