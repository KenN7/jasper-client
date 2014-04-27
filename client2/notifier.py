import Queue
import logging
import threading
import time
import client2.notifiersMod

class NotifierHandler:
    def __init__(self, mic, teller, profile, modules_names):
        self.queue = Queue.Queue()
        self.mic = mic
        self.teller = teller
        self.profile = profile
        self.modules_names = modules_names
        self.not_thread = None
        
    def start(self):
        self.not_thread = NotifierThread(self.modules_names,self.queue, self.mic, self.teller, self.profile)
        self.not_thread.start()
    
    def check(self):
        try:
            notif, module = self.queue.get(block=False)
            return notif, module
        except Queue.Empty:
            return None, None

    def action(self, module):
        module.handle()


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
            mod = getattr(client2.notifiersMod,mod)(self.mic, self.teller, self.profile)
            #mod = eval("hour.%s(self.mic, self.teller, self.profile)" % mod)
            return mod

        except Exception as e:
            logging.warn("Problem %s starting module %s" % (e,mod))
        
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
                    notif = module.notif_check()
                    self.queue.put((notif,module))
                    
                except Exception as e:
                    logging.warn('Problem %s with module %s' % (e,module))
            
            for i in xrange(60):
                if self.term:
                    break
                else:
                    time.sleep(1)

                    
    def stop(self):
        self.term = True
            

#just import this, instant NotifierHandler, start the thread and check 
#the submodules with check() method
