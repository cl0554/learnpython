#!/usr/bin/python
## encoding = "UTF-8"
import sys
import web

sys.path.append('.')
import apachexml
passwd_dict = {"mislost":"admin1234","falls":"123456"}
render = web.template.render('templates/')
urls = (
	'/login', 'index',
	'/addip', 'addip',
	'/delip', 'delip'
)

class index:
	def GET(self):	
		return render.login()

	def POST(self):
		apachexml.create_html()
		i = web.input()
		username = str(i.username)
		password = str(i.password)
		if username in passwd_dict.keys():
			if password == passwd_dict[username]:
				return render.show_ip()
			else:
		 		return render.login_failed()
		else:
			return render.username_errors()

class addip:
	def GET(self):
		return render.addip()

	def POST(self):
		i = web.input()
		name = i.name
		ip = i.ip
		apachexml.add_ip(ip, name)
		apachexml.create_html()
		return render.show_ip()

class delip:
	def GET(self):
		return render.delip()
		
	def POST(self):
		i = web.input()
		ip = i.ip
		apachexml.delete_ip(ip)
		apachexml.create_html()
		return render.show_ip()

			


if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()

	
