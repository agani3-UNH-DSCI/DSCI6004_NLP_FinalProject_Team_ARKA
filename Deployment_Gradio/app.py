#                                                                            Team ARKA
#                                                                          RAHUL MUVVALA
#                                                                         KALPANA CHAMALA
#                                                                       AJAY KUMAR GANIPINENI

import gradio as gr
import pandas as pd
import re
import pickle
import numpy as np
from keras_preprocessing.sequence import pad_sequences
from keras.models import load_model

# Load the trained model
model = load_model('Cyber_Bullying_Model.model')
classes = np.load('classes.npy')
f = open('tokenIzer.pickle', 'rb')
tokenizer = pickle.load(f)
f.close()

def preprocess_text(sen):
    sentence = remove_tags(sen)
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)
    sentence = re.sub(r'\s+', ' ', sentence)
    return sentence

TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)

def classify_text(text):
    # Preprocess the input text
    X = [preprocess_text(text)]
    X = tokenizer.texts_to_sequences(X)
    maxlen = 100
    X_test = pad_sequences(X, padding='post', maxlen=maxlen)
    
    # Make prediction
    pred = model.predict(X_test)
    predicted_class = classes[np.argmax(pred)]
    return predicted_class

# Create a Gradio interface
iface = gr.Interface(
    fn=classify_text,
    inputs="text",
    outputs="text",
    title="Cyber Bullying Detection",
    description="Enter a text and get the predicted class.",
    examples=[["I hate you!"], ["You're awesome!"]],
)

# Launch the Gradio interface
iface.launch()
