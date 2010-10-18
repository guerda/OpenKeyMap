#!/usr/bin/python
# -*- coding: UTF-8 -*-
from location import Location
import location
import re
import sys
from os import path
import urllib2
import json
from BeautifulSoup import BeautifulSoup, SoupStrainer

LIMIT_GEONAMES = 3000

"""
TODO
 - exclude first cities (top cities)

"""
offline = False #True

def get_location(city, country, state):
	if(offline):
		return {"lat": 51.0, "lon": 6.0}
	else:
		if state == None:
			url = "http://ws.geonames.org/searchJSON?q=%s&countryName=%s&maxRows=1" % (city, country)
		else:
			url = "http://ws.geonames.org/searchJSON?q=%s,%20%s&countryName=%s&maxRows=1" % (city, state, country)
		doc = urllib2.urlopen(url).read()
		result = json.loads(doc)
		if result["totalResultsCount"] == 0:
			lat, lon = 0, 0 
		else:
			first_hit = result['geonames'][0]
			lat = first_hit['lat']
			lon = first_hit['lng']
		return {"lat": lat, "lon": lon} 

def get_cities_from_biglumber():
	all_cities = []

	if offline:
		all_cities = location.createSampleList()	
	else:


		url = "http://biglumber.com/x/web?va=1"

		doc = urllib2.urlopen(url).read()
		# o for country, l for city, s for state
		links = SoupStrainer('a', href=re.compile(r'web\?s(o|l|s)=\d*'))
		soup = [str(elm) for elm in BeautifulSoup(doc, parseOnlyThese=links)]
		r = re.compile("<a href=\"([^\"]*)\">([^<]*)</a>")

	
		current_country = ""
		current_state = ""
		for line in soup:
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
	return all_cities

print "Download cities from BigLumber..."
all_cities = get_cities_from_biglumber()
print "Get geo position for all cities..."
if len(all_cities) > LIMIT_GEONAMES:
	print "Warning! Only the first %s cities will be displayed! Found: %d Cities" % (LIMIT_GEONAMES, len(all_cities))
# get geo position for all cities
i = 0
for city in all_cities:
	location = get_location(city.name, city.country, city.state)
	city.lat = location["lat"]
	city.lon = location["lon"]
	if (city.lat == 0.0) and (city.lon == 0.0):
		print city
	i += 1
	if i == LIMIT_GEONAMES: # Hit the geonames limit
		break

# initialize template engine

