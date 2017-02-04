import os
import sys
import time 
import urllib2
import xml.etree.ElementTree as ET
#import xml.etree.cElementTree as Ec
from lxml import etree as Ec
tree = ET.parse('stream.xml')
root = tree.getroot()
root1 = Ec.Element("ROOT")

#x = len(root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[0])
x = len(root.getchildren()[2].getchildren()[0].getchildren()[3])

for i in range (1,x):
	
	result = root.getchildren()[2].getchildren()[0].getchildren()[3].getchildren()[i]
	doc = Ec.SubElement(root1, "detector_details")
	Ec.SubElement(doc, "field1", name = "detector_ID").text = result.getchildren()[0].text
	Ec.SubElement(doc, "field2", name = "Status").text = result.getchildren()[1].text
tree1 = Ec.ElementTree(root1)
tree1.write("streamdata.xml", pretty_print=True, xml_declaration=True)
	
