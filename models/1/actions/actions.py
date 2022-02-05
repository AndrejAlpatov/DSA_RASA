"""
Module comprise implementation of two RASA-Intents:
Opening_time and Kiosk_menu_if
"""

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .data_for_actions import mensa_names, mensa_department_db
from random import randint
from .output_of_all_collections import data_bank_access
from .list_values_to_low_case import list_value_to_low_case


class ActionOpeningTimes(Action):
    """
    Class for action "Opening times" that say user when Caffe or Mensa i open
    """

    # return action object
    def name(self) -> Text:
        """
        Returns action object to rasa chat boot
        Returns:
            Returns action object
        """
        return "action_opening_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Answer to the user about opening time of cafe or mensa

        Args:
            dispatcher:
            tracker:
            domain:

        Returns:
            answer text to the user question e.g. Wann kann ich in der Mensa essen?
        """

        # get entity value from input
        mensa_department = next(tracker.get_latest_entity_values('mensa_department'), None)

        # If entity value is not defined
        if not mensa_department:
            msg = "Sie können auch eine bestimmte Abteilung angeben"
            dispatcher.utter_message(text=msg)
            return []

        # convert all characters to lowercase
        mensa_department_in_low_case = mensa_department.lower()

        # if entity value is not in DB
        if mensa_department_in_low_case not in mensa_department_db:
            msg = f"In der Mensa gibt es {mensa_department} nicht, oder vielleicht stimmt der Name nicht"
            dispatcher.utter_message(text=msg)
            return []

        # if entity value = "mensa"
        if mensa_department_in_low_case in mensa_names:
            msg = "Die Mensa hat von 11 Uhr 30 bis 14 Uhr geöffnet."
            dispatcher.utter_message(text=msg)
            return []
        else:  # if entity value = "kiosk"
            msg = "Von Montag bis Donnerstag ist der Kiosk von 8 bis 15 Uhr und freitags bis 14 Uhr geöffnet."
            dispatcher.utter_message(text=msg)
            return []


class ActionKioskMenuIf(Action):
    """
    Class for action kiosk_menu_if that returns user information about presents of goods in Kiosk
    """

    #
    def name(self) -> Text:
        """
        Returns action object to rasa chat boot
        Returns:
            Returns action object
        """
        return "action_kiosk_menu_if"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Returns answer to user question
        Args:
            dispatcher:
            tracker:
            domain:

        Returns:
            Answers to the question about presents of the goods in Caffe. e.g. Gibt es Coca-Cola am Kiosk?
        """

        # get entity value from input
        kiosk_menu = next(tracker.get_latest_entity_values('kiosk_menu'), None)

        # Get DB collections
        list_with_collections = data_bank_access(['kiosks_goods', 'answers', 'prompts'])
        db_collection = list_with_collections[0]
        db_collection_answers = list_with_collections[1]
        db_collection_prompts = list_with_collections[2]

        # Get documents from collections
        goods = db_collection.find_one({})
        answers = db_collection_answers.find_one({})
        prompts = db_collection_prompts.find_one({})

        # Get lists with positive und negative answers
        speech_text_positive_answers_list = answers['KIOSK_MENU_POSITIVE']
        speech_text_negative_answers_list = answers['KIOSK_MENU_NEGATIVE']

        # Put all good values in one list
        all_goods_orig = \
            goods['SWEETS'] + goods['HOT_DRINKS'] + goods['COLD_DRINKS'] + goods['FOOD'] + goods['SWEETS_WORD'] +\
            goods['DRINK_WORD'] + goods['FOOD_WORD']

        # convert data bank values to low case
        all_goods = list_value_to_low_case(all_goods_orig)
        sweets = list_value_to_low_case(goods['SWEETS'])
        hot_drinks = list_value_to_low_case(goods['HOT_DRINKS'])
        cold_drinks = list_value_to_low_case(goods['COLD_DRINKS'])
        food = list_value_to_low_case(goods['FOOD'])
        sweets_words = list_value_to_low_case(goods['SWEETS_WORD'])
        drink_words = list_value_to_low_case(goods['DRINK_WORD'])
        food_words = list_value_to_low_case(goods['FOOD_WORD'])

        # # If entity (slot) value is not defined
        if not kiosk_menu:
            msg = "Sie können einen bestimmten Produktnamen angeben "
            dispatcher.utter_message(text=msg)
            return []

        kiosk_menu_in_low_case = kiosk_menu.lower()

        # if the slot value is not in kiosk menu
        if kiosk_menu_in_low_case not in all_goods:
            msg = f"Am Kiosk gibt es {kiosk_menu} nicht, oder vielleicht stimmt der Name nicht"
            dispatcher.utter_message(text=msg)
            return []

        # If slot value has product name
        if kiosk_menu_in_low_case in sweets or kiosk_menu_in_low_case in hot_drinks or \
                kiosk_menu_in_low_case in cold_drinks or kiosk_menu_in_low_case in food:

            # Choose random answer from list
            list_index_ = randint(0, len(speech_text_positive_answers_list) - 1)
            msg = speech_text_positive_answers_list[list_index_] + f" {kiosk_menu.upper()} steht auf der Speisekarte"

            dispatcher.utter_message(text=msg)
            return []

        # If slot value has sweets product group name
        elif kiosk_menu_in_low_case in sweets_words:

            # Choose random answer from list
            list_index_ = randint(0, len(speech_text_positive_answers_list) - 1)
            msg = speech_text_positive_answers_list[list_index_] + ' ' + prompts['SWEET_CHOOSE']

            dispatcher.utter_message(text=msg)
            return []

        # If slot value has food product group name
        elif kiosk_menu_in_low_case in food_words:

            # Choose random answer from list
            list_index = randint(0, len(speech_text_positive_answers_list) - 1)
            msg = speech_text_positive_answers_list[list_index] + ' ' + prompts['FOOD_CHOOSE']

            dispatcher.utter_message(text=msg)
            return []

        # If slot value has drink product group name
        elif kiosk_menu_in_low_case in drink_words:

            # Choose random answer from list
            list_index = randint(0, len(speech_text_positive_answers_list) - 1)
            msg = speech_text_positive_answers_list[list_index] + ' ' + prompts['DRINK_CHOOSE']

            dispatcher.utter_message(text=msg)
            return []

        # default negative answers for other cases
        else:
            # Choose random answer from list
            list_index = randint(0, len(speech_text_negative_answers_list) - 1)
            msg = speech_text_negative_answers_list[list_index]

            dispatcher.utter_message(text=msg)
            return []
