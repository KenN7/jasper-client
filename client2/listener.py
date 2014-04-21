import logging
import json
import os

import CONFIG
import mic

class Listener:
    def __init__(self, lm, dic, perso_lm, perso_dic, mic):
        self.mic = mic
        self.profile = profile

    def run(self):
        while not self.term:
            sig, trans = self.mic.passiveListen(CONFIG.botname)
            logging.info("Threshold: %s, Translation: %s" % (sig,trans))
            if sig:
                inpt = self.mic.activeListen(sig)
                logging.info("Input: %s" % inpt)
                self.socket.send_json({'words': words})
            else:
                self.mic.say(CONFIG.pardon)

    def passiveListen(self):
        

    def stop(self):
        logging.info("Stoping listener")
        self.term = True

