import zmq
import logging
import json
import os

import CONFIG
import mic
import threading

logging.basicConfig(level=CONFIG.loglevel, filename="listener.log")
logger = logging.StreamHandler()
logger.setLevel(CONFIG.loglevel)
logging.getLogger().addHandler(logger)

class Listener(threading.Thread):
    def __init__(self, lm, dic, perso_lm, perso_dic):
        super().__init__()
        self.mic = mic.Mic(lm, dic, perso_lm, perso_dic)
        self.profile = profile
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind("ipc:///tmp/listener")
        self.term = False

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

    def stop(self):
        logging.info("Stoping listener")
        self.term = True

