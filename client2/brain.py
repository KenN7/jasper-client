#!/bin/python

import logging
from modules import *

class Brain(object):

    def __init__(self, mic, profile):
        """
        Instantiates a new Brain object, which cross-references user
        input with a list of modules. Note that the order of brain.modules
        matters, as the Brain will cease execution on the first module
        that accepts a given input.

        Arguments:
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone number)
        """
        self.mic = mic
        self.profile = profile
        self.modules = [
            Gmail, Notifications, Birthday, Weather, HN, News, Time, Joke, Life]

    def query(self, text):
        """
        Passes user input to the appropriate module, testing it against
        each candidate module's isValid function.

        Arguments:
        text -- user input, typically speech, to be parsed by a module
        """
        for module in self.modules:
            if module.isValid(text):
                logging.warn('module %s is valid' % module)
                try:
                    module.handle(text, self.mic, self.profile)
                    logging.warn('going True')
                    return True

                except Exception as e:
                    logging.error("Error in module, %s" % e)
                    self.mic.say(
                        "I'm sorry. I had some trouble with that operation. Please try again later.")
            else:
                continue
        return False
