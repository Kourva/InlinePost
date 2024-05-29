# -*- coding: utf-8 -*-

"""
Helper script for main script contains helper function
"""

# Standard library modules
from typing import NoReturn, Dict, List, Union
import json

# Third-Party modules
from telebot.types import User

class TgUser:
    """
    TgUser class for telegram user
    """
    def __init__(self, from_user: User) -> NoReturn:
        """
        Initialize method to get parameters

        :params: TeleBot's User type
        :return: None (typing.NoReturn)
        """
        self.fn: str = from_user.first_name   # First name
        self.ln: str = from_user.last_name    # Last name
        self.un: str = from_user.username     # User name
        self.id: int = from_user.id           # Chat ID

    def valid_identifier(self) -> Union[str, int]:
        """
        Method to get valid identifier in user data

        :params: None
        :return: string or integer of user identifier
        """
        return self.fn or self.un or self.id

    def mention(self) -> str:
        """
        Method to return user mention tag

        :params: None
        :return: string of user mention
        """
        return f"[{self.valid_identifier()}](tg://user?id={self.id})"

def config_loader() -> Dict[str, Union[str, int]]:
    """
    Helper function to return configuration

    :params: None
    :return: Configuration in dictionary type
    """
    # Load configuration
    with open("config.json", "r") as config_file:
        return json.load(config_file)