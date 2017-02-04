import os
import sys
import time 
import urllib2
import xml.etree.ElementTree as ET
tree = ET.parse('stream.xml')
root = tree.getroot()
#x = len(root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[0])
x = len(root.getchildren()[2].getchildren()[0].getchildren()[3])
for i in range (1,x):
	result = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
	
	print result.getchildren()[0].text, '|', result.getchildren()[1].text
print x