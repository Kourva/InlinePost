#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Simple poster bot  to post your  content
# to channels and add inline buttons to it

# Standard library modules
from typing import NoReturn, Dict, List, Union

# Third-Party modules
from telebot import types, TeleBot
from telebot.util import quick_markup

# Local application modules
from utils import config_loader, TgUser

# Load configs
config: Dict[str, Union[str, int]] = config_loader()

# Initialize the bot
bot : TeleBot = TeleBot(config["token"])
bot_info: types.User = bot.get_me()
print(f"The Bot is online (id: {bot_info.id}) \33[0;32m[Normal]\33[m...")

# Start command handler ( /start )
@bot.message_handler(commands=["start"])
def start_command_handler(message: types.Message) -> NoReturn:
    """
    Start command handler to handle /start command in bot

    :params: Telebot's Message type
    :return: None (typing.NoReturn)
    """
    # Get user details and create user object
    user: TgUser = TgUser(message.from_user)
    tbot: TgUser = TgUser(bot_info)

    # Make markup button for bot action
    markup: quick_markup = quick_markup({
        "Add to channel": {
            "url": f"t.me/{tbot.un}?startchannel&admin=permission"
        }
    })

    # Print welcome message to user
    bot.send_chat_action(chat_id=message.chat.id, action="typing")
    bot.reply_to(
        message=message,
        text=(
            f"Hello {user.mention() or user.valid_identifier()}\n\n"
            f"Welcome to {tbot.mention()} \\! Enjoy\\.",
        ),
        parse_mode="MarkdownV2",
        reply_markup=markup
    )

# Help command handler ( /help )
@bot.message_handler(commands=["help"])
def help_command_handler(message: types.Message) -> NoReturn:
    """
    Help command handler to handle /start command in bot

    :params: Telebot's Message type
    :return: None (typing.NoReturn)
    """
    # Get user details and create user object
    user: TgUser = TgUser(message.from_user)
    tbot: TgUser = TgUser(bot_info)

    # Print welcome message to user
    bot.send_chat_action(chat_id=message.chat.id, action="typing")
    bot.reply_to(
        message=message,
        text=(
            f"Hello {user.mention() or user.valid_identifier()}\n\n"
            f"Only you need is adding {tbot.mention()} to channel as admin via "
            f"inline button \\(tap /start\\)\n\nThen simply send message to "
            f"bot and then reply your inline keyboard data to message: \n"
            f"Example:\nboost: t\\.me/username\\?boost\nvisit: t\\.me/example\n\n"
            f"This is a simple and not\\-feature rich bot and may contains bugs and "
            f"creepy ERRORS\\!\\!\nFeel free to issue btw :\\)\n\nMay i added "
            f"more option to the bot in next updates\\!",
        ),
        parse_mode="MarkdownV2",
        link_preview_options=types.LinkPreviewOptions(is_disabled=True)
    )


# Message handler
@bot.message_handler(func=lambda msg: msg.chat.type=="private" and msg.reply_to_message)
def start_command_handler(message: types.Message) -> NoReturn:
    """
    Message handler to handle replied messages

    :params: Telebot's Message type
    :return: None (typing.NoReturn)
    """
    # Get replied data
    replied_data: List[str] = message.text.strip().split("\n")
    
    # Make markup using replied data
    markup: quick_markup = quick_markup({(
        item.split(":", maxsplit=1)[0].strip()): {
            "url": item.split(":", maxsplit=1)[1].strip()
        } for item in replied_data
    })

    # Send edited message to channel
    bot.send_message(
        chat_id=config["channel"],
        text=message.reply_to_message.text,
        reply_markup=markup
    )


# Run the bot
if __name__ == '__main__':
    bot.infinity_polling(
        skip_pending=True
    )
