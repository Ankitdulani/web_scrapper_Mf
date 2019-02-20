from bs4 import BeautifulSoup 

class Beautysoup:

	soup=None

	def __inti__ (self):
		print("BeautifulSoup class")

	def parseHTML(self, html_doc):
		self.soup=BeautifulSoup(html_doc,'html.parser')
		# print(self.soup.prettify())

	def findLinks(self):
		links=[]
		for link in self.soup.find_all("a"):

			#chechking the links are duplicate'
			url=link.attrs['href']
			if url not in links:
				links.append(url)

		return links

	def getInformation(self):

		#Dictionary 
		D={}

		#Extracting Body From the content
		body_tag=self.soup.body

		# Using the Format from the link to Extract information 
		row_tag=body_tag.find("div", {'class':['row']}).find_next("div", {'class':['row']})
		col12_tag=row_tag.next_element

		web_Align_tag=col12_tag.find("div",{'class': ['container', 'web-align', '']})
		mfName_tag=web_Align_tag.find("div",{'class': ['mfNameWrapper']})

		# extracting the name of mutual Fund
		name_tag=mfName_tag.find("h1",{'class':{'fundName'}})
		D["name"]=name_tag.contents[0]

		type_tag=mfName_tag.next_sibling

		# extracting type based on market
		a_tag=type_tag.find("div",{'class': ['tagDiv']})
		D["Type_market"]=a_tag.contents[0]

		#extracting type based fund size
		a_tag=a_tag.find_next("div",{'class': ['tagDiv']})
		D["Type_size"]=a_tag.contents[0]


		web_Align_tag=web_Align_tag.find_next("div",{'class':['web-align']})
		find1Section_tag=web_Align_tag.find("div",{'id': 'fnd1Section'})


		#extracting Risk, Min Sip,expense Ratio,NAV, Fund Started, Fund size
		for table_tag in find1Section_tag.find_all("table"):
		    for row in table_tag.find_all("tr"):
		        key = row.find("th")
		        value =row.find("td")
		        D[key.contents[0]]=value.contents[0]


		col12_tag=find1Section_tag.parent

		#relevant Data list
		relevantHeading={'Returns','Holding Analysis','Top 10 Holdings'}
		
		relevant_tags=self.extractRelevantTags(col12_tag,relevantHeading)            

		
			#extracting returns
		self.extractReturn(relevant_tags['Returns'],D)

		# extracting top 10 holding
		self.extractTopTenHolding(relevant_tags['Top 10 Holdings'],D)

		## Extract Holding Analysis
		self.extractAnalysis(relevant_tags['Holding Analysis'],D)

		# extraction other informatiomnm
		self.extractStats(relevant_tags['Holding Analysis'],D)

		
			

		return (D)

	def extractRelevantTags(self, col12_tag , relevantHeading ):

		relevant_tags={}

		#extracting relevant tag
		for divSection_tag in col12_tag.find_all("div",{"class":"divSections"}):
		    
		    #sepreating the required Data
		    componentsMainHeading=divSection_tag.find("h2",{"class":"componentsMainHeading"})
		    if componentsMainHeading != None:
		    	
		        heading=componentsMainHeading.contents[0]
		        if heading in relevantHeading:
		            relevant_tags[heading]=divSection_tag

		return relevant_tags           

	def extractReturn(self, Returns_tag,D):

		year_list={}
		for para15_tag in Returns_tag.find_all("div",{"class":"para15"}):
		        t_list=para15_tag.attrs['class']
		        if "center-align" in t_list:
		            year_list[para15_tag.span.contents[0]]="0"

		            
		count=0
		return_list=[]
		for heading15_tag in Returns_tag.find_all("div",attrs={"class":["heading15"]}):
		    t_list=heading15_tag.attrs['class']
		    if "center-align" in t_list:
		        return_list.append(heading15_tag.contents[0])
		        
		itr =iter(return_list)
		for k,v in year_list.items():
		    year_list[k]=next(itr)
		    
		D.update(year_list)   

	def extractAnalysis(self, Analysis_tag,D):
		#extracting equity Sector allocation
		pie_tag=Analysis_tag.find("div",{"class":"pieHeadingDiv"})
		pie_tag=pie_tag.find("div",{"class":"pieDiv"})


		equityAllocation_list=[]

		for allocation in pie_tag.find_all("div",{"class":"pieDiv2"}):
		    sector_tuple=[]
		    sector=allocation.find(style="font-weight: 500;").contents[0]
		    per=allocation.find("div",{"class":"makePara"}).contents[0]
		    sector_tuple.append(sector)
		    sector_tuple.append(per)
		    equityAllocation_list.append(sector_tuple)
		    
		D["equitySectorAllocation"]=equityAllocation_list

	def extractTopTenHolding(self, Holding_tag,D ):
		
		table_tag=Holding_tag.find("table")

		thead_tag=table_tag.find("thead")
		tbody_tag=table_tag.find("tbody")

		holding_list=[]

		for row in tbody_tag.find_all("tr"):
		    temp_list=[]
		    for col in row.find_all("td"):
		        temp_list.append(col.contents[0])
		    holding_list.append(temp_list)

		D["topHolding"]=holding_list

	def extractStats(self, Analysis_tag, D ):

		Row=[]
		Row.append(Analysis_tag.find("div",{"class":"holdFirstRow"}))
		Row.append(Analysis_tag.find("div",{"class":"holdSecondRow"}))

		for row_tag in Row:
		    for e in row_tag.find_all("div",{"class":"col l4"}):
		        value=e.find("div",{"class":"holdingText"}).contents[0]
		        parameter=e.find("div",{"class":"holdingPara"}).contents[0]
		        D[parameter]=value


