import logging
import time
from client2.modules_classes import NotifierModule

class Hour(NotifierModule):
    def notif_check(self):
        new_time = time.ctime().split(' ')[3]
        self.last_time = new_time
        if int(new_time[6:]):
            logging.warn('returning %s' % new_time)
            return new_time
        else:
            logging.warn('returning None')
            return None

    def handle(self):
        self.teller.say(self.last_time)
