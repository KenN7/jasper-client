# -*- coding: utf-8 -*-

import random
import re

WORDS = ["sens", "de", "la", "vie"]


def handle(text, teller, mic, profile):
    """
        Responds to user-input, typically speech text, by relaying the
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (input)
        profile -- contains information related to the user (e.g., phone number)
    """
    messages = ["C'est 42, évidement !",
                "42, c'est assez logique pourtant !"]

    message = random.choice(messages)

    teller.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r"\bsens (de la vie|de l'univers)\b", text, re.IGNORECASE))
