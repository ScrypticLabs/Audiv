# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2018-02-16 21:04:55
# @Last Modified by:   Abhi
# @Last Modified time: 2018-02-16 22:34:28

from fbchat import Client
from fbchat.models import *

class Facebook:
	def __init__(self, email, password):
		self.user = Client(email, password)
		self.name = self.user.name
		self.id = self.user.uid

	def sendMessage(self, recipient, message, threadType = ThreadType.GROUP):
		self.user.send(Message(text=message, thread_id=self.getThreadID(recipient), thread_type=threadType))

	def getChats(self, n = 20):
		threads = self.user.fetchThreadList()
		threads += client.fetchThreadList(offset=n, limit=10)
		print("Threads: {}".format(threads))

	
	def logout(self):
		self.user.logout()




