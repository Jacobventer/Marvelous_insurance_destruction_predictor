#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Extract feautures
import xml.etree.ElementTree as ET
from datetime import datetime
import pandas as pd

#Features used by the trained model
MODEL_FEATURES = ["credit_score", "num_properties", "age"]

def extract_features_from_xml(xml_string: str) -> dict:
    #Features selected
    features = {
        "credit_score": None,
        "age": None,
        "num_superpowers": 0,
        "num_properties": 0,
        "num_credit_cards": 0,
        "total_credit_limit": 0,
        "xml_parse_error": 0
    }

    try:
        root = ET.fromstring(xml_string)

        #Credit Score
        credit_score = root.find("CreditScore")
        if credit_score is not None and credit_score.text:
            features["credit_score"] = int(credit_score.text)

        #Age
        dob = root.find("DateOfBirth")
        if dob is not None and dob.text:
            birth_date = datetime.strptime(dob.text, "%Y-%m-%d")
            today = datetime.today()
            features["age"] = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)) #calc age today

        #Superpowers
        powers = root.find("SuperPowers")
        if powers is not None:
            features["num_superpowers"] = len(powers.findall("item"))

        #Properties
        props = root.find("PropertiesOwnedBySuperhero")
        if props is not None:
            features["num_properties"] = len(props.findall("item"))

        #Credit Cards
        cards = root.find("CreditCards")
        if cards is not None:
            card_items = cards.findall("item")
            features["num_credit_cards"] = len(card_items)

            for card in card_items:
                limit = card.find("CreditLimit")
                if limit is not None and limit.text:
                    features["total_credit_limit"] += int(limit.text)

    except ET.ParseError:
        print("Warning: Malformed XML detected.") #warning added for safety net
        features["xml_parse_error"] = 1

    return features


def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:

    parsed = df["CreditInfo"].apply(extract_features_from_xml)
    feature_df = pd.json_normalize(parsed)

    return pd.concat([df, feature_df], axis=1)


# In[ ]:




