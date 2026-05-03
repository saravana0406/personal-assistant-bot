import numpy as np
import pickle
import json
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load data
with open("data/intents.json") as file:
    data = json.load(file)

sentences = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        sentences.append(pattern)
        labels.append(intent["tag"])

# Tokenizer
tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences)

# Label encoding
le = LabelEncoder()
labels_encoded = le.fit_transform(labels)

# Model
model = Sequential()
model.add(Embedding(1000, 64, input_length=padded.shape[1]))
model.add(LSTM(64))
model.add(Dense(32, activation="relu"))
model.add(Dense(len(set(labels_encoded)), activation="softmax"))

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Train
model.fit(padded, labels_encoded, epochs=300, verbose=1)

# Save model
model.save("model/chatbot_model.h5")

pickle.dump(tokenizer, open("model/tokenizer.pkl", "wb"))
pickle.dump(le, open("model/label_encoder.pkl", "wb"))

print("Training completed and model saved.")