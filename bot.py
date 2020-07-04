#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi {}! i\'m a bot that will allow you to see all the Regions on Sale easily! \n '
                              'For see all commands type /help'     .format(update.message.from_user.first_name))
 

def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(""
                               "/start - For restart the bot\n\n"
                               "/add - or you can contact @Denver \n\n" 
                               "/moon - for see the regions on moon\n\n"
                               "/earth - for see the regions on earth\n\n"  
                               "/donate - For make a Donation "
                               "")
                             
    
def moon_command(update, context):
    """Send a message when the command /regions is issued."""
    update.message.reply_text('No Offers ! ')
    
def add_command(update, context):
    """Send a message when the command /add is issued."""
    update.message.reply_text('For add your product please contact @Denver02 ')
    
def earth_command(update, context):
    """Send a message when the command /ressources is issued."""
    update.message.reply_text(" EARTH REGIONS ON SALE!\n\n"
                              "State + North Vietnam + South Vietnam\n" "Link: https://m.rivalregions.com/#state/details/3049\n" "Price: 300T\n" " Contact: @kilicArslanHan\n\n"
                              "------------------------------------------------------------\n"
                              "Region: region Eastern Afghanistan\n" "Link: https://m.rivalregions.com/#map/details/16102\n" "Price: >> Contact: @RuhAdam1\n\n" )
    
def donate_command(update, context):
    """Send a message when the command /accounts is issued."""
    update.message.reply_text('Mobile Link:\n https://m.rivalregions.com/#slide/profile/142452277391688 \n\n PC Link:\n https://rivalregions.com/#slide/profile/142452277391688')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text('Invalid Command, Please type /help for see all command!')
    



def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1365071054:AAGjPvFsFh9uWfPWn698ZEkBqoEGAtyX7Mw", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("add", add_command))
    dp.add_handler(CommandHandler("moon", moon_command))
    dp.add_handler(CommandHandler("earth", earth_command))
    dp.add_handler(CommandHandler("donate", donate_command))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
