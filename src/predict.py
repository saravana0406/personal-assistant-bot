import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model("model/chatbot_model.h5")
tokenizer = pickle.load(open("model/tokenizer.pkl", "rb"))
le = pickle.load(open("model/label_encoder.pkl", "rb"))

def predict_class(text):

    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=10)

    result = model.predict(padded, verbose=0)

    index = np.argmax(result)
    confidence = np.max(result)

    tag = le.inverse_transform([index])[0]

    print("User Input:", text)
    print("Predicted Intent:", tag)
    print("Confidence:", confidence)

    # IMPORTANT FIX
    if confidence < 0.60:
        return "unknown"

    return tag