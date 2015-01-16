#!/usr/bin/env python
from xml.dom import minidom

dom = minidom.parse('name.xml')
root = dom.documentElement

nodes = root.childNodes

for node in nodes:
	print '*********************************'
	for i in node.childNodes:
		if i.nodeType == node.ELEMENT_NODE:
			tag = i.nodeName
			content = i.childNodes[0].data
			#print '%s : %s' % (i.nodeName,  i.childNodes[0].data)
			print '%s: %s' % (tag, content)
