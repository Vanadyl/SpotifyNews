# -*- coding: utf-8 -*-

import os
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
TEXT_ANALYTICS_SUBSCRIPTION_KEY = 'abd1652d64b84172b9a3e316c558f4e6'

subscription_key = TEXT_ANALYTICS_SUBSCRIPTION_KEY

TEXT_ANALYTICS_ENDPOINT = 'https://spotifytextanalysis.cognitiveservices.azure.com/'

endpoint = TEXT_ANALYTICS_ENDPOINT

def authenticateClient():
    credentials = CognitiveServicesCredentials(subscription_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credentials=credentials)
    return text_analytics_client
def sentiment(TextToTest):
    
    client = authenticateClient()

    try:
        documents = [
            {"id": "1", "language": "en", "text": TextToTest},
        ]

        response = client.sentiment(documents=documents)
        for document in response.documents:
            print("Document Id: ", document.id, ", Sentiment Score: ",
                  "{:.2f}".format(document.score))

    except Exception as err:
        print("Encountered exception. {}".format(err))


def key_phrases(TextToTest):
    
    client = authenticateClient()

    try:
        documents = [
            {"id": "1", "language": "en", "text": TextToTest},
        ]

        for document in documents:
            print(
                "Asking key-phrases on '{}' (id: {})".format(document['text'], document['id']))

        response = client.key_phrases(documents=documents)

        for document in response.documents:
            print("Document Id: ", document.id)
            print("\tKey Phrases:")
            for phrase in document.key_phrases:
                print("\t\t", phrase)

    except Exception as err:
        print("Encountered exception. {}".format(err))


TextToTestt = "Prosecutors say the man accused of murdering Grace Millane disposed of her body using the case."
sentiment(TextToTestt)
key_phrases(TextToTestt)