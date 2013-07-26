import urllib2
from bs4 import BeautifulSoup

website = urllib2.urlopen("http://www.123teachme.com/spanish_verb_conjugation/hacer")
soup = BeautifulSoup(website)

table = soup.table
trs = list(soup.table.find_all('tr'))
trsfiltered = []
for tr in trs:
	tds = list(tr.find_all('td'))
	if tds[0]['class'][0] == 'tense_heading':
		trsfiltered.append(tr)

for tr in trsfiltered:
	tds = list(tr.find_all('td'))
	print tds[2].text
