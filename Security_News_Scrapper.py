# Import libraries
from urllib.request import urlopen as uReq
import requests
import bs4
import csv
from datetime import date


class bleeping_computer:

	def Bleeping_Computer(self):
	# Set the URL you want to webscrape from
		url = "https://www.bleepingcomputer.com/news/security/" 
		#Get Connection
		response = requests.get(url, verify=False)
		# Parse Page
		page_content = response.text
		soup = bs4.BeautifulSoup(page_content, 'lxml')
		section = soup.find_all('section', class_='bc_main_content')
		for elem in section:
		    wrappers = elem.find_all('ul', {"id": "bc-home-news-main-wrap"})
		    for x in wrappers: 
		        detail = x.find_all('li')
		        for row in detail:
		            for l in row.find_all('div', class_='bc_latest_news_text'):
		                text = l.find('h4').get_text() 
		                value = l.find('p').get_text().encode("utf-8")
		                date = l.find('ul').get_text()
		                link = l.find('a')
		                #print(text)
		                #print(value)
		                #print(link)
		                #print(date)
		                #print("-------")

#Initiate Class
bleepingcomputer_init = bleeping_computer()
bleepingcomputer_init.Bleeping_Computer()

class hacker_news:

	def home(self):
		url = "https://thehackernews.com/" 
		#Get Connection
		response = requests.get(url, verify=False)

		# Parse Page
		page_content = response.text
		soup = bs4.BeautifulSoup(page_content, 'html.parser')
		section = soup.find_all('main', class_='main clear')

		#Get Date
		date_today = date.today().strftime("%d/%m/%Y")

		#Write Data to CSV
		with open('Cybersecurity_news.csv', mode='a', newline='') as csv_file:
			fieldnames = ['Title','Description', 'Date', 'Front Page']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			writer.writeheader()
			for elem in section:
			    wrappers = elem.find_all('div', class_='left-box')  
			    for x in wrappers: 
			        detail = x.find_all('div', class_='content section')
			        for row in detail:
			            for l in row.find_all('div', class_='body-post clear'):
			                link_raw = l.find('a')
			                link = link_raw.get('href')
			                text_raw = l.find('h2').get_text().encode('ascii',errors='ignore')
			                text = text_raw.decode('ascii')
			                test = l.find('div', class_='item-label').get_text().encode('ascii',errors='ignore')	
			                result = l.find('i', class_='icon-font icon-calendar').findNextSibling(text=True)		
			                writer.writerow({'Title': text, 'Description': link, 'Date': result })
			                print(result)
			                print(link)
			                print(text)
			                print("******************************************** Hacker News Front Page")

	def breaches(self):
		url = "https://thehackernews.com/search/label/data%20breach" 
		#Get Connection
		response = requests.get(url, verify=False)

		# Parse Page
		page_content = response.text
		soup = bs4.BeautifulSoup(page_content, 'html.parser')
		section = soup.find_all('main', class_='main clear')

		#Get Date
		date_today = date.today().strftime("%d/%m/%Y")

		#Write Data to CSV
		with open('Cybersecurity_news.csv', mode='a', newline='') as csv_file:
			fieldnames = ['Title','Description', 'Date', 'Data Breach']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			writer.writeheader()
			for elem in section:
			    wrappers = elem.find_all('div', class_='left-box')  
			    for x in wrappers: 
			        detail = x.find_all('div', class_='content section')
			        for row in detail:
			            for l in row.find_all('div', class_='body-post clear'):
			                link_raw = l.find('a')
			                link = link_raw.get('href')
			                text_raw = l.find('h2').get_text().encode('ascii',errors='ignore')
			                text = text_raw.decode('ascii')
			                test = l.find('div', class_='item-label').get_text().encode('ascii',errors='ignore')	
			                result = l.find('i', class_='icon-font icon-calendar').findNextSibling(text=True)		
			                writer.writerow({'Title': text, 'Description': link, 'Date': result })
			                print(result)
			                print(link)
			                print(text)
			                print("********************************************Data Breach")


	def cyberattacks(self):
		url = "https://thehackernews.com/search/label/Cyber%20Attack" 
		#Get Connection
		response = requests.get(url, verify=False)

		# Parse Page
		page_content = response.text
		soup = bs4.BeautifulSoup(page_content, 'html.parser')
		section = soup.find_all('main', class_='main clear')

		#Get Date
		date_today = date.today().strftime("%d/%m/%Y")

		#Write Data to CSV
		with open('Cybersecurity_news.csv', mode='a', newline='') as csv_file:
			fieldnames = ['Title','Description', 'Date', 'CyberAttacks']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			writer.writeheader()
			for elem in section:
			    wrappers = elem.find_all('div', class_='left-box')  
			    for x in wrappers: 
			        detail = x.find_all('div', class_='content section')
			        for row in detail:
			            for l in row.find_all('div', class_='body-post clear'):
			                link_raw = l.find('a')
			                link = link_raw.get('href')
			                text_raw = l.find('h2').get_text().encode('ascii',errors='ignore')
			                text = text_raw.decode('ascii')
			                test = l.find('div', class_='item-label').get_text().encode('ascii',errors='ignore')	
			                result = l.find('i', class_='icon-font icon-calendar').findNextSibling(text=True)		
			                writer.writerow({'Title': text, 'Description': link, 'Date': result })
			                print(result)
			                print(link)
			                print(text)
			                print("******************************************** cyberattacks")


	def vulnerabilities(self):
		url = "https://thehackernews.com/search/label/Vulnerability" 
		#Get Connection
		response = requests.get(url, verify=False)

		# Parse Page
		page_content = response.text
		soup = bs4.BeautifulSoup(page_content, 'html.parser')
		section = soup.find_all('main', class_='main clear')

		#Get Date
		date_today = date.today().strftime("%d/%m/%Y")

		#Write Data to CSV
		with open('Cybersecurity_news.csv', mode='a', newline='') as csv_file:
			fieldnames = ['Title','Description', 'Date', 'Vulnerability']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			writer.writeheader()
			for elem in section:
			    wrappers = elem.find_all('div', class_='left-box')  
			    for x in wrappers: 
			        detail = x.find_all('div', class_='content section')
			        for row in detail:
			            for l in row.find_all('div', class_='body-post clear'):
			                link_raw = l.find('a')
			                link = link_raw.get('href')
			                text_raw = l.find('h2').get_text().encode('ascii',errors='ignore')
			                text = text_raw.decode('ascii')
			                test = l.find('div', class_='item-label').get_text().encode('ascii',errors='ignore')	
			                result = l.find('i', class_='icon-font icon-calendar').findNextSibling(text=True)		
			                writer.writerow({'Title': text, 'Description': link, 'Date': result})
			                print(result)
			                print(link)
			                print(text)
			                print("******************************************** Vulnerability")

#Initiate Class
hacker_news_init = hacker_news()
hacker_news_init.home()
hacker_news_init.breaches()
hacker_news_init.cyberattacks()
hacker_news_init.vulnerabilities()
