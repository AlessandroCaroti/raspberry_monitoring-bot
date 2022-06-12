#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import re
from typing import List
import requests, os, json

from telegram import (InlineKeyboardButton, Bot,
                      InlineKeyboardMarkup, Update)
from telegram.ext import (Updater,
                          CommandHandler,
                          CallbackQueryHandler, CallbackContext)
from telegram.utils.request import Request
import requests

import version
import config.config as config
import lib.permission as perm
from lib.storage import (read_machines_file, read_commands_file)
from lib.types import Machine
from lib.utils import (find_by_name)
import time

logging.basicConfig(
    format=config.LOG_FORMAT,
    level=config.LOG_LEVEL)
logger = logging.getLogger(__name__)
from gpiozero import CPUTemperature, LoadAverage
import psutil


def main() -> None:
    #if not config.VERIFY_HOST_KEYS:
    #    logger.warning(
    #        'Verification of host keys for SSH connections is deactivated.')
    #global machines
    #global commands
    #machines = read_machines_file(config.MACHINES_STORAGE_PATH)
    #commands = read_commands_file(config.COMMANDS_STORAGE_PATH)
    #perm.load_users()
#
    ## Set up bot
    #req = Request(con_pool_size=8, connect_timeout=8)
    #my_bot = Bot(config.TOKEN, request=req)
    #updater = Updater(bot=my_bot, use_context=True)
    #dispatcher = updater.dispatcher
#
    ## Add commands info
    #cmd = [("help", "Display commands"),
    #       ("wake", "Wake saved machine"),
    #       ("list", "List all saved machines"),
    #       ("ping", "Ping a server")]
    #my_bot.set_my_commands(cmd)

    # Create menu Keyboards TODO: add shutdown
    
    
    # Add handlers
    
    
    
    #dispatcher.add_error_handler(error)
#
    ## Start bot
    #updater.start_polling()
    #updater.idle()
    cpu = CPUTemperature()
    la = LoadAverage()
    while True:
        time.sleep(5)
        print("\n-------------------------------------------\n\tGPIZERO")
        print(cpu.temperature)
        print(la.load_average)
        print(la.value)
        print(str(int(LoadAverage(minutes=1).load_average*100))+"%")
        print("\n-------------------------------------------\n\tPSUTILS")
        print('The CPU usage is: ', psutil.cpu_percent(4))
        
        # Getting % usage of virtual_memory ( 3rd field)
        print('RAM memory % used:', psutil.virtual_memory()[2])
        
        load1, load5, load15 = psutil.getloadavg()
        cpu_usage = (load15/os.cpu_count()) * 100
        print("The CPU usage is : ", cpu_usage)
        print("=====================================================\n\n")

        


if __name__ == '__main__':
    main()
