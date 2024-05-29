#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library imports
import typing

# Related third party imports
from telebot import types, TeleBot
import telebot

# Local application/library specific imports
import utils

# Connect to bot
# Token placed in utils.py file. You can change it with your token
bot: TeleBot = TeleBot(utils.config_loader()["token"])
print(f"The Bot is online (id: {bot.get_me().id}) \33[0;31m[Command Installer]\33[m...")

# Set bot commands
print("[!] Configuring bot commands...")
bot.set_my_commands(
    commands=[
        types.BotCommand(
            command="start",
            description="Start the bot"
        ),
        types.BotCommand(
            command="help",
            description="Show help message"
        )
    ]
)
print("[!] Commands successfully configured.\n[!] Run main.py")