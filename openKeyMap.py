#!/usr/bin/python
import urllib2
import re
from BeautifulSoup import BeautifulSoup, SoupStrainer

url = "http://biglumber.com/x/web?va=1"

doc = urllib2.urlopen(url).read()
links = SoupStrainer('a', href=re.compile(r'web\?s(o|l)=\d*'))
soup = [str(elm) for elm in BeautifulSoup(doc, parseOnlyThese=links)]
for elm in soup:
	print elm
