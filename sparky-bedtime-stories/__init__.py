from os.path import join, abspath, dirname
import os.path
import random
from adapt.tools.text.tokenizer import EnglishTokenizer
from mycroft.messagebus.client.ws import WebsocketClient
from mycroft.messagebus.message import Message
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft.util import play_mp3
from mycroft.util.parse import fuzzy_match
from mycroft.util.parse import match_one
from mycroft.audio import wait_while_speaking
from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.context import *

class BedtimeStories(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self):
        
        #Register list of story titles that are held in a padatious entity
        self.register_entity_file("title.entity")
        self.process = None
        
        #Build story list

    #Play random story from list
    @intent_file_handler('stories.bedtime.intent')
    def handle_stories_bedtime(self, message):
	pass

    #Pick story by title
    @intent_file_handler('pick.story.intent')
    def handle_pick_story(self, message):
	pass

    #List stories in library
    @intent_file_handler('list.stories.intent')
    def handle_list_stories(self, message):
	pass
    
    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process.wait()

def create_skill():
    return BedtimeStories()

