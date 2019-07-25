from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler
from mycroft.util.log import LOG
from mycroft.util.parse import extract_number, normalize

import random
import re

class DiceSkill(MycroftSkill):

    def __init__(self):
        super(DiceSkill, self).__init__(name="DiceSkill")

    @intent_file_handler("Dice.intent")
    def handle_roll_dice_intent(self, message):
	pass

    @intent_file_handler("NormalDice.intent")
    def handle_roll_normal_intent(self, message):
	pass
            
    def roll(self, dice_count, dice_range, modificator):
	pass

    @intent_file_handler("Range.intent")
    def handle_generate_number_intent(self, message):
	pass

def create_skill():
    return DiceSkill()
