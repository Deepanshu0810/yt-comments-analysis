import tensorflow as tf
from keras_preprocessing.text import text_to_word_sequence
from keras_preprocessing.sequence import pad_sequences
from keras.datasets import imdb
from keras.models import load_model
import numpy as np

# Load the model
model = load_model('../model/sentiment_analysis_model.h5')
MAX_LENGTH = 250
VOCAB_SIZE = 10000

# Load the word index
word_index = imdb.get_word_index()

def encode_input(text):
    # Convert text to sequence of words
    words = text_to_word_sequence(text)
    # Convert words to index
    word_indices = [word_index[word] if word in word_index else 0 for word in words]
    # Pad sequence
    padded_sequence = pad_sequences([word_indices], maxlen=MAX_LENGTH, padding='post', value=VOCAB_SIZE)
    return padded_sequence

def predict_sentiment(text):
    # Encode input
    encoded_text = encode_input(text)
    # Predict sentiment
    prediction = model.predict(encoded_text)
    # Return label
    if prediction[0] < 0.5:
        return 'Negative'
    else:
        return 'Positive'