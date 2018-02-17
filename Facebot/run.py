# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2018-02-10 01:50:40
# @Last Modified by:   Abhi
# @Last Modified time: 2018-02-16 21:00:39

# import fbchat
# from getpass import getpass
# username = "abhi.gupta.37819"
# client = fbchat.Client(username, getpass())
# no_of_friends = 1
# for i in range(no_of_friends):
#     name = "knlyyl"
#     friends = client.getUsers(name)  # return a list of names
#     friend = friends[0]
#     msg = "HOLA"
#     sent = client.send(friend.uid, msg)
#     if sent:
#         print("Message sent successfully!")


from fbchat import Client
from fbchat.models import *

client = Client('abhisoccerplayer@live.ca',)

print('Own id: {}'.format(client.uid))

for i in range(100):
	client.send(Message(text='Hi from Abhis mac for the '+str(i)+'th time!'), thread_id="100005961453176", thread_type=ThreadType.USER)

# Fetches a list of all users you're currently chatting with, as `User` objects
users = client.fetchAllUsers()

print("users' IDs: {}".format(user.uid for user in users))
print("users' names: {}".format(user.name for user in users))

client.logout()