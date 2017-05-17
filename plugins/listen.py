# -*- coding: utf-8 -*-
"""
Created on Thu May 18 01:46:37 2017

@author: kikumi
"""

import random
#発言に反応するデコーダ
from slackbot.bot import listen_to

"""テキストファイルの内容を読み込んで返信
"""
#ファイルを開く
responses = []
rfile = open("plugins/dict/singasong.txt", "r", encoding = "utf-8")
r_lines = rfile.readlines()
rfile.close()
for line in r_lines:
    str = line.rstrip("¥n")
    if (str!=""):
        responses.append(str)

@listen_to("あいたくて")
@listen_to("会いたくて")
def sing_func(message):
    message.send(random.choice(responses))
    message.reply("うるせー！！！")

@listen_to("おなかすいた")
def listen_func(message):
    message.send("うるせー！！")
    message.reply("土でも食ってろ！")
