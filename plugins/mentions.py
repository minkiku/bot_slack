# -*- coding: utf-8 -*-
"""
Created on Mon May 15 01:27:11 2017

@author: kikumi
"""
import random
# @xxxx: で反応するデコーダ
from slackbot.bot import respond_to
#該当する応答がない場合に反応するデコーダ
#from slackbot.bot import default_reply

"""テキストファイルの内容を読み込んで返信
"""
#ファイルを開く
responses = []
rfile = open("plugins/dict/dull.txt", "r", encoding = "utf-8")
r_lines = rfile.readlines()
rfile.close()
for line in r_lines:
    str = line.rstrip("¥n")
    if (str!=""):
        responses.append(str)

@respond_to("ねむい")
@respond_to("くそねむい")
@respond_to("ねむい！")
def mention_func(message):
    message.reply(random.choice(responses))

        
"""「いいね！」を含む返信
"""
@respond_to("かっこいい")
def cool_func(message):
    message.reply("何言ってだおまえ")
    message.react("+1")

