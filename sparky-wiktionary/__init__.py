from mycroft import MycroftSkill, intent_file_handler
from mycroft.audio import wait_while_speaking
from mycroft.skills.context import *
from wiktionaryparser import WiktionaryParser
from mycroft.util.log import LOG


class WiktionarySkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
	pass

    @intent_file_handler('fallback.wiktionary.definition.intent')
	pass

def create_skill():
    return WiktionarySkill()

