#!/bin/python

import logging
import client2.modules

class Brain(object):

    def __init__(self, teller, mic, profile, modules):
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
        self.teller = teller
        self.modules_names = modules
        self.modules = []
        self.start_modules()

    def add_mod(self, mod):
        try:
            mod = getattr(client2.modules,mod)(self.mic, self.teller, self.profile)
            return mod
        except Exception as e:
            logging.warn('Problem %s with module %s' % (e,mod))

    def start_modules(self):
        for module in self.modules_names:
            logging.warn('appening module %s' % module)
            self.modules.append(self.add_mod(module))

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
                    module.handle(text, self.teller, self.mic, self.profile)
                    logging.warn('going True')
                    return True

                except Exception as e:
                    logging.error("Error in module, %s" % e)
                    self.teller.say(
                        "I'm sorry. I had some trouble with that operation. Please try again later.")
            else:
                continue
        return False



class ConversationModule(object):
    def __init__(self, mic, teller, profile):
        self.WORDS = []
        self.mic = mic
        self.teller = teller
        self.profile = profile
        
    def handle(self, text):
        logger.warn('Not yet implemented')
        
    def isValid(self, text):
        logger.warn('Not yet implemented')
        return False

