# -*- coding: utf-8 -*-
# @Author: Abhi
# @Date:   2018-02-16 21:04:49
# @Last Modified by:   Abhi
# @Last Modified time: 2018-02-16 22:37:56

from facebook import *

if __name__ == "__main__":
	user = Facebook("abhisoccerplayer@live.ca", "devfest")
	user.getChats()