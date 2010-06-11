#!/usr/bin/bash
# -*- coding: UTF-8 -*-
class Location:
	"Constructor to build Locations easily"
	def __init__(self, p_name, p_country):
		self.name = p_name
		self.country = p_country
		self.state = None

	def __repr__(self):
		if self.state == None:
			return "%s in %s (%d,%d)" % (self.name, self.country, 0, 0)
		else:
			return "%s in %s, %s (%d,%d)" % (self.name, self.state, self.country, 0, 0)

def createSampleList():
	list = []
	list.append(Location("Viersen", "Germany"))
	list.append(Location("München", "Germany"))
	l = Location("New York", "USA")
	l.state = "NY"
	list.append(l)
	return list

if __name__ == "__main__":
	print "test"
	print createSampleList()
