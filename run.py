# -*- coding: utf-8 -*-
"""
Created on Mon May 15 01:25:00 2017

@author: kikumi
"""

from plugins import listen
from plugins import mentions

from slackbot.bot import Bot

def main():
    bot = Bot()
    bot.run()
    
if __name__ == "__main__":
    print("start..")
    main()
