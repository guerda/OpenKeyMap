#!/usr/bin/bash
# -*- coding: UTF-8 -*-
class Location:
	"Constructor to build Locations easily"
	def __init__(self, p_name, p_country):
		self.name = p_name
		self.country = p_country
		self.state = None
		self.lat = 0.0
		self.lon = 0.0

	def __repr__(self):
		if self.state == None:
			return "%s in %s (%d;%d)" % (self.name, self.country, self.lat, self.lon)
		else:
			return "%s in %s, %s (%d;%d)" % (self.name, self.state, self.country, self.lat, self.lon)

	def __hash__(self):
		return ("%s#%s#%s" % (self.name, self.state, self.country)).__hash__()
		

def createSampleList():
	"""
	Creates a short list of sample cities, with all options:
		* including city and country,
		* including state and
		* including lat & lon
	"""
	list = []

	list.append(Location("Viersen", "Germany"))

	list.append(Location("München", "Germany"))

	l = Location("New York", "USA")
	l.state = "NY"
	list.append(l)

	l = Location("Buxtehude", "Germany")
	l.lat = 49.0
	l.lon = 7.3
	list.append(l)

	return list

if __name__ == "__main__":
	print "Prnting a short example list"
	print createSampleList()
