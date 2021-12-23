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

mensa_department_db = ['Kiosk', 'Cafeteria', 'Mensa', 'in der Mensa', 'am Kiosk', 'in Mensa', 'mensa', 'kiosk', 'cafeteria',
                       'in der mensa', 'am kiosk', 'in mensa']
kiosk_names = ['Kiosk', 'Cafeteria', 'am Kiosk', 'kiosk', 'cafeteria', 'am kiosk']
mensa_names = ['Mensa', 'in der Mensa', 'in Mensa', 'mensa', 'in der mensa', 'in mensa']


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

        if mensa_department not in mensa_department_db:
            msg = f"In der Mensa gibt es {mensa_department} nicht, oder vielleicht stimmt der Name nicht"
            dispatcher.utter_message(text=msg)
            return []

        if mensa_department in mensa_names:
            msg = "Die Mensa hat von 11 Uhr 30 bis 14 Uhr geöffnet."
            dispatcher.utter_message(text=msg)
            return []
        else:
            msg = "Von Montag bis Donnerstag ist der Kiosk von 8 bis 15 Uhr und freitags bis 14 Uhr geöffnet.."
            dispatcher.utter_message(text=msg)
            return []
