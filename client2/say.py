#!/bin/python

#import pyttsx
from espeak import espeak

class Speak:
    def __init__(self):
#        self.engine = pyttsx.init()
#        self.engine.setProperty('voice', 'mb-fr1')
#        self.engine.setProperty('rate', 140)
        espeak.set_voice('mb-fr1')
        espeak.set_parameter(1, 140) # 1 represents the speed of the voice
#
    def say(self, phrase):
        espeak.synth(phrase)
#        self.engine.say(phrase)
#        self.engine.runAndWait()
#
#    def volume(self, prop):
#        volume = self.engine.getProperty('volume')
#
#        self.engine.setProperty('volume', volume+0.25*prop)
#        if prop:
#            self.say('Plus fort !')
#        else:
#            self.say('Moins fort !')
