#!/usr/bin/python
# -*- coding: UTF-8 -*-
from location import Location
import location
import re
import sys
from os import path
from cPickle import * 
import urllib2
import json
"""
TODO
 - exclude first cities (top cities)

"""
offline = False #True

def get_location(city, country, state):
	if(offline):
		url = "http://ws.geonames.org/searchJSON?q=%s&country=%s&maxRows=1&adminCode1=%s" % (city, country, state)
		doc = urllib2.urlopen(url).read()	
		print json.loads(doc)
	else:
		return None

all_cities = []

if offline:
	all_cities = location.createSampleList()	
else:

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

#print all_cities

print "Get geo position for all cities..."
# get geo position for all cities
for city in all_cities:
	get_location(city.name, city.country, city.state)
	break

# initialize template engine

