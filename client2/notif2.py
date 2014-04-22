import Queue
import logging
import threading
import time

class NotifierHandler:
    def __init__(self, mic, teller, profile, modules_names):
        self.queue = Queue.Queue()
        self.mic = mic
        self.teller = teller
        self.profile = profile
        self.modules_names = modules_names
        
    def start(self):
        not_thread = NotifierThread(self.modules_names,self.queue, self.mic, self.teller, self.profile)
        not_thread.start()
    
    def check(self):
        try:
            m = self.queue.get(block=False)
            return m
        except Queue.Empty:
            return None

class NotifierThread(threading.Thread):
    def __init__(self, modules_names, queue, mic, teller, profile):
        super(NotifierThread, self).__init__()
        self.queue = queue
        self.mic = mic
        self.teller = teller
        self.profile = profile
        self.modules_names = modules_names
        self.modules = []
        self.term = False
        
    def add_mod(self, mod):
        try:
            #mod = getattr('notif2',mod)(self.mic, self.teller, self.profile)
            mod = eval("%s(self.mic, self.teller, self.profile)" % mod)

        except Exception as e:
            logging.warn("Problem %s starting module %s" % (e,mod))
        return mod
        
    def start_modules(self):
        for module in self.modules_names:
            logging.warn('appening module %s' % module)
            self.modules.append(self.add_mod(module))
        
    def run(self):   
        self.start_modules()
        while not self.term:
            for module in self.modules:
                try:
                    logging.warn('dealing with %s' % module)
                    self.queue.put(module.notif_check())
                except Exception as e:
                    logging.warn('Problem %s with module %s' % (e,module))
            time.sleep(10)
                    
    def stop(self):
        self.term = True
            

class NotifierModule(object):
    def __init__(self, mic, teller, profile):
        self.term = False
        self.mic = mic
        self.teller = teller
        self.profile = profile
        self.last_time = None
                
    def notif_check(self):
        logging.warn("Not yet implemented")
        new_time = None
        self.last_time = new_time
        result = None
        return result
        
class a(NotifierModule):
    def __init__(self, mic, teller, profile):
        super(a, self).__init__(mic, teller, profile)

    def notif_check(self):
        new_time = 0
        self.last_time = 0
        result = 20
        time.sleep(5)
        return result
        
#just import this, instant NotifierHandler, start the thread and check 
#the submodules with check() method
