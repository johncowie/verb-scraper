import urllib2
from bs4 import BeautifulSoup

website = urllib2.urlopen("http://www.123teachme.com/spanish_verb_conjugation/hacer")
soup = BeautifulSoup(website)

table = soup.table
trs = list(soup.table.find_all('tr'))
for tr in trs:
	# print tr
	tds = list(tr.find_all('td'))
	print tds[0].text
