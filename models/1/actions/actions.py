# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .data_for_actions import mensa_names, mensa_department_db, kiosk_products
from src.data_bank_functions.output_of_all_collections import data_bank_access


class ActionOpeningTimes(Action):

    def name(self) -> Text:
        return "action_opening_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mensa_department = next(tracker.get_latest_entity_values('mensa_department'), None)

        if not mensa_department:
            msg = "Sie können auch eine bestimmte Abteilung angeben"
            dispatcher.utter_message(text=msg)
            return []

        mensa_department_in_low_case = mensa_department.lower()

        if mensa_department_in_low_case not in mensa_department_db:
            msg = f"In der Mensa gibt es {mensa_department} nicht, oder vielleicht stimmt der Name nicht"
            dispatcher.utter_message(text=msg)
            return []

        if mensa_department_in_low_case in mensa_names:
            msg = "Die Mensa hat von 11 Uhr 30 bis 14 Uhr geöffnet."
            dispatcher.utter_message(text=msg)
            return []
        else:
            msg = "Von Montag bis Donnerstag ist der Kiosk von 8 bis 15 Uhr und freitags bis 14 Uhr geöffnet."
            dispatcher.utter_message(text=msg)
            return []


class ActionKioskMenuIf(Action):

    def name(self) -> Text:
        return "action_kiosk_menu_if"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

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

        if not kiosk_menu:
            msg = "Sie können auch einen bestimmteт Produktnamen angeben "
            dispatcher.utter_message(text=msg)
            return []

        kiosk_menu_in_low_case = kiosk_menu.lower()

        if kiosk_menu_in_low_case not in kiosk_products:
            msg = f"Am Kiosk gibt es {kiosk_menu} nicht, oder vielleicht stimmt der Name nicht"
            dispatcher.utter_message(text=msg)
            return []

        if kiosk_menu_in_low_case in mensa_names:
            msg = "Die Mensa hat von 11 Uhr 30 bis 14 Uhr geöffnet."
            dispatcher.utter_message(text=msg)
            return []
        else:
            msg = "Von Montag bis Donnerstag ist der Kiosk von 8 bis 15 Uhr und freitags bis 14 Uhr geöffnet."
            dispatcher.utter_message(text=msg)
            return []

        # If slot value has product name
        if food_type in goods['SWEETS'] or food_type in goods['HOT_DRINKS'] or food_type in goods['COLD_DRINKS']:
            # Zufällige Antwortauswahl aus der Liste
            list_index = randint(0, len(speech_text_positive_answers_list) - 1)
            speech_text = speech_text_positive_answers_list[list_index]

        # If slot value has sweets product group name
        elif food_type in goods['SWEETS_WORD']:
            list_index = randint(0, len(speech_text_positive_answers_list) - 1)
            speech_text = speech_text_positive_answers_list[list_index] + ' ' + prompts['SWEET_CHOOSE']

        # If slot value has food product group name
        elif food_type in goods['FOOD_WORD']:
            list_index = randint(0, len(speech_text_positive_answers_list) - 1)
            speech_text = speech_text_positive_answers_list[list_index] + ' ' + prompts['FOOD_CHOOSE']

        # If slot value has drink product group name
        elif food_type in goods['DRINK_WORD']:
            list_index = randint(0, len(speech_text_positive_answers_list) - 1)
            speech_text = speech_text_positive_answers_list[list_index] + ' ' + prompts['DRINK_CHOOSE']
