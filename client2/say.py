#!/bin/python

import pyttsx

class Speak:
    def __init__(self):
        self.engine = pyttsx.init()

    def say(self, phrase):
        self.engine.say(phrase)
        self.engine.runAndWait()

    def volume(self, prop):
        volume = self.engine.getProperty('volume')

        self.engine.setProperty('volume', volume+0.25*prop)
        if prop:
            self.say('Plus fort !')
        else:
            self.say('Moins fort !')
