import csv
import xml.etree.ElementTree as ET
from collections import Counter


parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()
xml_items = root.findall("channel/item")
temp_list = []
string = ""
for item in xml_items:
	string += item.find("description").text
words = string.split()
for letters in words:
  if len(letters) > 6:
    temp_list.append(letters)
print(Counter(temp_list).most_common(10))