import json
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def load_data():
    with open('data/intents.json') as file:
        data = json.load(file)
    return data

def preprocess_data(data):
    sentences = []
    labels = []

    for intent in data['intents']:
        for pattern in intent['patterns']:
            sentences.append(pattern)
            labels.append(intent['tag'])

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(sentences)
    sequences = tokenizer.texts_to_sequences(sentences)

    padded = pad_sequences(sequences)

    return padded, labels, tokenizer