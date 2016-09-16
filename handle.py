# _*_ coding: utf-8 _*_
# filename: handle.py

import hashlib
import web

class Handle(object):
	def GET(self):
		try:
			data = web.input()
			if len(data) ==0:
				return "hello this is a handle view"
			signature = data.signature
			timestamp = data.timestamp
			nonce = data.nonce
			echostr = data.echostr
			token = "xiaohu"
			
			list = [token, timestamp,nonce]
			list.sort()
			sha1 = hashlib.sha1()
			map(sha1.update,list)
			hashcode = sha1.hexdigest()
			print "handle/GET func: hashcode, signature:", hashcode,signature
			if hashcode == signature
				return ecostr
			else:
				return ""
			except Exception, Argument:
				return Argument