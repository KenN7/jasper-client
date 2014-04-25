#/bin/python

import yaml
import sys
import logging, logging.handlers

from client2 import mic
from client2 import say
from client2 import brain
from client2.notifiersMod import notifier

from client2 import CONFIG

class Jaspi:
    def __init__(self, profile, mic, teller):
        self.mic = mic    
        self.teller = teller
        self.profile = yaml.safe_load(open(profile,'r'))
        self.teller.say("Bonjour, je suis %s, ravis de vous revoir" % CONFIG.botname)
        self.brain = brain.Brain(self.teller, self.mic, self.profile)
        self.notifier = notifier.NotifierHandler(mic, teller, profile, CONFIG.modules)
        self.notifier.start()
        self.state = 0
        logging.warn("Bot started ...")

    def run(self):
        while True:
            logging.warn("While loop running ...")
            try:
                logging.warn("state %i" % self.state)
                if self.state == -1:
                    notif, module = self.notifier.check()
                    if module is not None:
                        self.notifier.action(module)
                        logging.warn('Got notification : %s' % notif)
                    else:
                        self.state = 0

                elif self.state == 0:
                    th, trans = self.mic.passiveListen(CONFIG.botname)
                    if trans==CONFIG.botname:
                        logging.warn('Detected botname:')
                        logging.warn(trans)
                        self.state = 1
                        logging.warn('going to state 1')
                    elif th==False:
                        logging.warn('Detected False:')
                        self.state = -1
                    else:
                        logging.warn('detected : %s' % th)
                        self.state = -1

                elif self.state == 1:
                    detection = self.mic.activeListen()
                    done = self.brain.query(detection)
                    logging.warn('done: %s' % done)
                    logging.warn('detected : %s' % detection)
                    if not done:
                        self.teller.say("Je n ai pas compris.")
                        logging.warn('Pas compris ...')
                    self.state = -1
                
            except KeyboardInterrupt:
                logging.warn("Terminating ...")
                self.notifier.not_thread.stop()
                break
            

if __name__ == "__main__":

    logging.basicConfig(level=CONFIG.loglevel)
    log_filename = "jaspi.log"
    fh = logging.handlers.TimedRotatingFileHandler(log_filename, when='h')
    fh.setLevel(CONFIG.loglevel)
    fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(fh_formatter)
    logging.getLogger("").addHandler(fh)

    logging.warn("-------------------------------")
    logging.warn("Welcome to Viki, voice enabled assistant")
    logging.warn("Copyright 2014 Ken Hasselmann")
    logging.warn("Forked from Jasper by Shubhro Saha & Charlie Marsh")
    logging.warn("-------------------------------")
    
    mic_ = mic.Mic(CONFIG.lm, CONFIG.dic, CONFIG.perso_lm, CONFIG.perso_dic, CONFIG.hmdir)    
    teller = say.Speak() 
    Jaspi = Jaspi(CONFIG.profile, mic_, teller)
    Jaspi.run()
