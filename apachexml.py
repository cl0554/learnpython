#!/usr/bin/env python
import os
import sys
import shutil
from xml.dom import minidom

doc = minidom.parse('test.xml')
root = doc.documentElement
nodes = root.childNodes

def show_xml(user=None, value=None):
	if user:
		s = get_user_list()
		if user in s:
			for node in nodes:
				if node.nodeType == node.ELEMENT_NODE:	
					if node.getAttribute('name') == user:
						print node.getAttribute('name')
						for i in node.childNodes:
							if i.nodeType == node.ELEMENT_NODE:
								print i.childNodes[0].data
		else:
			print "Errors!Don't have %s user!" % user 
	else:	
		for node in nodes:
			if node.nodeType == node.ELEMENT_NODE:
				if value:
					print '# ' + node.getAttribute('name')
				else:
					print node.getAttribute('name')
				for i in node.childNodes:
					if i.nodeType == node.ELEMENT_NODE:
						if value:
							print 'Allow from ' + i.childNodes[0].data 
						else:
							print i.childNodes[0].data
def create_conf():
	output=sys.stdout
	outputfile = open('./conf/proxy.conf', 'w')
	sys.stdout = outputfile
	s1 = '''<IfModule mod_proxy.c>
        ProxyRequests On
        <Proxy *>
           AddDefaultCharset off
           #Require all denied
           #Require local
           Order deny,allow
           Deny from all''' + '\n'*2 + '#'*80 + '\n'
 
	s2 = '\n' + '#'*80 + '\n'*2 + '''       </Proxy>\n\n</IfModule> '''
	
	print s1
	show_xml(value=True)
	print s2
	outputfile.close()
	sys.stdout = output

def create_html():
	output=sys.stdout
	outputfile = open('/root/learngit/html/templates/show_ip.html', 'w')
	sys.stdout = outputfile
	print '<a href="addip">ADD IP</a>'
	show_xml()
	outputfile.close()
	sys.stdout = output



def delete_ip(ip):
	for node in nodes:
                if node.nodeType == node.ELEMENT_NODE:
                        for i in node.childNodes:
                                if i.nodeType == node.ELEMENT_NODE:
					if ip == i.childNodes[0].data:
						i.parentNode.removeChild(i)
	f = open('test.xml', 'w')
	doc.writexml(f)
	f.close()
	delblankline()

def add_ip(ip,name=None):
	userlist = get_user_list()
	iplist = get_ip_list()
    	if ip in iplist : 
        	print '%s is already exist!' % ip
       		return False

	if name:
		if name in userlist:
			for node in nodes:
				if node.nodeType == node.ELEMENT_NODE:	
					if node.getAttribute('name') == name:
						newtag = doc.createElement('ip')
						newtext = doc.createTextNode(ip)
						head = doc.createTextNode('\t')
						end = doc.createTextNode('\n\t')
						node.appendChild(head)
						node.appendChild(newtag)
						node.childNodes[-1].appendChild(newtext)
						node.appendChild(end)	
	
		else:
			print 'Errors!Don\'t hava this user!'
        		return False
	else:
		print 'Errors!Must input user!'	
        	return False

	f = open('test.xml', 'w')
	doc.writexml(f)	
	f.close()						
	return True	
	


def get_user_list():
	user_list = []
	for node in nodes:
		if node.nodeType == node.ELEMENT_NODE:
			username = node.getAttribute('name')
			user_list.append(username)	
	return user_list

def get_ip_list():
	ip_list=[]
	for node in nodes:
		if node.nodeType == node.ELEMENT_NODE:
                       	for i in node.childNodes:
                               	if i.nodeType == node.ELEMENT_NODE:
	                               	 ip_l = i.childNodes[0].data
					 ip_list.append(ip_l)
	return ip_list

def delblankline(infile='test.xml', outfile='test.tmp'):
	infp = open(infile, 'r')
	outfp = open(outfile, 'w')
	lines = infp.readlines()
	for li in lines:
		if li.split():
			outfp.writelines(li)
	infp.close()
	outfp.close()
	shutil.copy(outfile,infile)
	
def add_user(adduser):
	head_person = doc.createTextNode('\t')
	end_person = doc.createTextNode('\n')
	newuser = doc.createElement('person')
	newattribute = doc.createAttribute('name')
	root.appendChild(head_person)
	root.appendChild(newuser)
	root.childNodes[-1].appendChild(end_person)
	root.childNodes[-1].setAttribute('name', adduser)
	root.appendChild(end_person)
	f = open('test.xml', 'w')
	doc.writexml(f)
	f.close()
	
	


if __name__ == '__main__':
	#while True:
#		user = raw_input('Input username:')
#		show_xml(user)
  	#create_conf()
	
	#delete_ip('192.168.1.1')
	add_ip('8.8.8.8', 'mislost')
	#get_ip_list()
	#delete_ip('192.168.1.1')
	#delblankline('test.xml','test.tmp')
	#add_user('mislost')
	create_html()

