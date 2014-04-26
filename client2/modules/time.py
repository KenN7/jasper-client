import datetime
import re
from app_utils import getTimezone
from semantic.dates import DateService
from client2.brain import ConversationModule

class Time(ConversationModule):
    def __init__(self, mic, teller, profile):
        super(Time, self).__init__(mic, teller, profile)
        self.WORDS = ['heure']

    def handle(text, teller, mic, profile):
        """
            Reports the current time based on the user's timezone.

            Arguments:
            text -- user-input, typically transcribed speech
            mic -- used to interact with the user (input)
            profile -- contains information related to the user (e.g., phone number)
        """

        tz = getTimezone(profile)
        now = datetime.datetime.now(tz=tz)
        service = DateService()
        response = service.convertTime(now)
        teller.say("Il est %s." % response)


    def isValid(text):
        """
            Returns True if input is related to the time.

            Arguments:
            text -- user-input, typically transcribed speech
        """
        return bool(re.search(r'\bheure\b', text, re.IGNORECASE))
