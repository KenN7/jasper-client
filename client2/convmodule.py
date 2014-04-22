import logging

    
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

class test(ConversationModule):
    def __init__(self, mic, teller, profile):
        super(test, self).__init__(mic, teller, profile)
        self.WORDS = ['test', 'fre']

    def handle(self, text):
        logging.warn('handle method from instance test with mic:%s and words:%s' % (self.mic,self.WORDS))

    def isValid(self, text):
        return True


