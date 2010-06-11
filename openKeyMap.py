#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Location import Location
import Location
"""
TODO
 - exclude first cities (top cities)

"""
offline = True

all_cities = []

if offline:
	all_cities = Location.createSampleList()	
else:
	import urllib2
	import re
	from BeautifulSoup import BeautifulSoup, SoupStrainer

	url = "http://biglumber.com/x/web?va=1"

	doc = urllib2.urlopen(url).read()
	# o for country, l for city, s for state
	links = SoupStrainer('a', href=re.compile(r'web\?s(o|l|s)=\d*'))
	soup = [str(elm) for elm in BeautifulSoup(doc, parseOnlyThese=links)]
	r = re.compile("<a href=\"([^\"]*)\">([^<]*)</a>")

	
	current_country = ""
	current_state = ""
	for line in soup:
	#	print line
		m = r.match(line)
		if m != None:
			href = m.group(1)
			name = m.group(2)
			if href.find("?so=") > -1:
				current_country = name[:-1]
			elif href.find("?ss=") > -1:
				current_state = name[:-1]
			else:
				all_cities.append(Location(name, current_country))
				if current_country == "USA":
					all_cities[-1].state = current_state

print all_cities




