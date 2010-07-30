#!/usr/bin/python
# -*- coding: UTF-8 -*-
from location import Location
import location
from os import path
import pickle
"""
TODO
 - exclude first cities (top cities)

"""
offline = True

all_cities = []

if offline:
	all_cities = location.createSampleList()	
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
# Dictionary of list
tmp_city = Location("Viersen","Germany")
tmp_city.lat = 51.0
tmp_city.lon = 6.1
cached_cities = {}
# TODO convert to function?
cached_cities[tmp_city.__hash__()] = tmp_city
f = open("location.cache",'wb')
pickle.dump(cached_cities, f)
f.close()
del cached_cities

# load cache --> pickle?
if(path.exists("location.cache")):
	f = open("location.cache","rb")
	cached_cities = pickle.load(f)
	f.close()

print cached_cities

print "Get geo position for all cities"
# get geo position for all cities
for city in all_cities:
	if cached_cities.has_key(city.__hash__()):
		tmp_cached_city = cached_cities[city.__hash__()]
		print tmp_cached_city
		city.lat = tmp_cached_city.lat
		city.lon = tmp_cached_city.lon
	else:
		pass
		#set up request to geonames
		# add to cache

print "Geo positions found:"
print all_cities

# save geo position in cache --> pickle?
# initialize template engine
