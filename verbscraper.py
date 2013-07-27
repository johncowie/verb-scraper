import urllib2, re, sys
from bs4 import BeautifulSoup

website = urllib2.urlopen("http://www.123teachme.com/spanish_verb_conjugation/" + sys.argv[1])
soup = BeautifulSoup(website)

table = soup.table
trs = list(soup.table.find_all('tr'))
trsfiltered = []
headTds = ['tenses', 'english', '1s', '2s', '3s', '1p', '2p', '3p']

for tr in trs:
	tds = list(tr.find_all('td'))
	if tds[0]['class'][0] == 'tense_heading':
		trsfiltered.append(tr)

for tr in trsfiltered:
	tds = list(tr.find_all('td'))
	print re.sub('\W+', '-', tds[0].text.lower()) + ':'
	for i in range(1, len(tds)):
		if len(re.sub('\W+', '', tds[i].text)) != 0:
			print "\t" + headTds[i] + ": " + tds[i].text.replace('OR', ' / ')


