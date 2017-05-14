# -*- coding: utf-8 -*-
"""
Created on Mon May 15 01:27:11 2017

@author: kikumi
"""

# @xxxx: で反応するデコーダ
from slackbot.bot import respond_to
#発言に反応するデコーダ
from slackbot.bot import listen_to
#該当する応答がない場合に反応するデコーダ
from slackbot.bot import default_reply

@respond_to("こんにちは〜")
def mention_func(message):
    message.reply("おまえ誰だよ")

@listen_to("おなかすいた")
def listen_func(message):
    message.send("うるせー！！")
    message.reply("土でも食ってろ！")
    
@respond_to("かっこいい")
def cool_func(message):
    message.reply("何言ってだおまえ")
    message.react("+1")
    

@respond_to(r"^ping\s+\d+\.\d+\.\d+\.\d+\s*$")
def ping_func(message):
    message.reply("ping実行すんなし")
