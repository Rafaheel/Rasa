# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import pathlib

from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

names = pathlib.Path("data/db_nomes.txt").read_text().split("\n")



class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_first_name(
        self,
        slot_value: Any,        
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Primeiro nome foi = {slot_value} e o tamanho foi = {len(slot_value)}")        
        first_name = tracker.slots.get("first_name")
        if len(slot_value) <= 2:            
            dispatcher.utter_message(text=f"Esse é um nome muito pequeno, tente novamente.")           
            return {"first_name": None}
                   
        else:
            if first_name not in names:                
                dispatcher.utter_message(text=f"É um prazer conhecer você {slot_value}, mas seu nome não esta na lista.")
            return {"first_name": slot_value}

    def validate_last_name(
        self,
        slot_value: Any,        
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        print(f"O sobre nome foi = {slot_value} e o tamanho foi = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"Esse é um sobrenome é muito pequeno, tente novamente.")
            return {"last_name": None}
        else:
            return {"last_name": slot_value}
