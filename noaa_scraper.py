import requests
import json
from bs4 import BeautifulSoup

# NOAA Storm Events Search
# All Storm Events in Florida between 07-01-2018 and 07-05-2019
url = ""\
"https://www.ncdc.noaa.gov/stormevents/listevents.jsp?"\
"eventType=ALL&"\
"beginDate_mm=07&beginDate_dd=01&beginDate_yyyy=2018&"\
"endDate_mm=07&endDate_dd=05&endDate_yyyy=2019&"\
"county=ALL&"\
"hailfilter=0.00&tornfilter=0&windfilter=000&"\
"sort=DT&"\
"submitbutton=Search&"\
"statefips=12%2CFLORIDA"

# get the page
page = requests.get(url)

# parse the page into soup object
soup = BeautifulSoup(page.text, "lxml")

# find the table with id="results"
results = soup.find('table', { 'id': 'results' })

# find all table rows
rows = results.find_all('tr')

# find all headers in top row, extract title attribute from each <a> 
titles = [th.a['title'].strip() for th in rows[0].find_all('th')]

# find all data
data = []
for tr in rows:
	# find all data elements, strip spaces
	values = [td.text.strip() for td in tr.find_all('td')]   #list comprehension
	#data.append( json.dumps(values) ) # transform to json
	data.append(values)

sz = len(data)
# data[0] and data[1] are junk, data[sz-1] is totals; slice them out
data = data[2:sz-1]

print( json.dumps(titles) )
print( json.dumps(data) )
