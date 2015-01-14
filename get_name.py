#!/usr/bin/python

import web
passwd_dict = {"mislost":"admin1234","falls":"123456"}
render = web.template.render('templates/')
urls = (
	'/login','index'
)

class index:
	def GET(self):	
		return render.login()

	def POST(self):
		i = web.input()
		
		username = str(i.username)
		password = str(i.password)
		#login(username,password)
		if username in passwd_dict.keys():
			if password == passwd_dict[username]:
				return render.login_success()
			else:
		 		return render.login_failed()
		else:
			return render.username_errors()
		

		#return render.index(name=i.username,i.password)
#
#def auth(username,password):
#	if password == passwd_dict[username]:
#		return render.login_success() 
#	else: 
#		return render.login_failed()
#
#def login(username,password):
#	if username in passwd_dict.keys():
#		auth(username,password)
#	else:
#		return render.username_errors()	
	

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()

	
