#/bin/python

import yaml
import sys
import logging

import mic
import listener
import listener_com
import brain
import notifier

import CONFIG
"""
put in config :
("languagemodel.lm", "dictionary.dic",
              "languagemodel_persona.lm", "dictionary_persona.dic"

              yaml.safe_load(open("profile.yml", "r"))

"""

class Jaspi:
    def __init__(self, lm, dic, perso_lm, perso_dic, profile):
        self.mic = mic.Mic(lm, dic, perso_lm, perso_dic)    
        self.profile = yaml.safe_load(open(profile),'r')
        self.mic.say("Hello I'm Jaspi, Nice heering from you")
        self.brain = brain.Brain(self.mic, self.profile)
        self.notifier = notifier.Notifier(self.profile)

    def run(self):
        while True:
            spoken_words = listener_com.Listen()
            
            logging.info("Let's go ...")
            try:
                for phrase in spoken_words:
                   self.brain.query(phrase)

            except KeyboardInterrupt:
                logging.info("Terminating ...")
            

if __name__ == "__main__":

    logging.info("-------------------------------")
    logging.info("Welcome to Jaspi, voice enabled assistant")
    logging.info("Copyright 2014 Ken Hasselmann")
    logging.info("Forked from Jasper by Shubhro Saha & Charlie Marsh")
    logging.info("-------------------------------")
 
    Jaspi = Jaspi(CONFIG.lm, CONFIG.dic, CONFIG.perso_lm, CONFIG.perso_dic, CONFIG.profile)
    listener_thread = listener.Listener(CONFIG.lm, CONFIG.dic, CONFIG.perso_lm, CONFIG.perso_dic)
    listener_thread.start()
    Jaspi.run()
    listener_thread.stop()
