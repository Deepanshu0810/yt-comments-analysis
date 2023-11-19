import tensorflow as tf
from keras_preprocessing.text import text_to_word_sequence
from keras_preprocessing.sequence import pad_sequences
from keras.datasets import imdb
from keras.models import load_model
import numpy as np
import pickle

# Load the model
model = load_model('../model/sentiment_analysis_model.h5')
MAX_LENGTH = 250
VOCAB_SIZE = 10000

# Load the word index
# word_index = imdb.get_word_index()

with open('../model/tokenizer.pickle','rb') as f:
    word_index = pickle.load(f)

def encode_input(comment_list):
    # Convert comment to sequence of words
    encoded_list = [text_to_word_sequence(comment) for comment in comment_list]
    # Replace words with integers
    encoded_list = [[word_index[word] if word in word_index else 0 for word in comment] for comment in encoded_list]
    # Pad sequences
    encoded_list = pad_sequences(encoded_list, maxlen=MAX_LENGTH, padding='post',value=VOCAB_SIZE-1)
    # Return encoded list
    return encoded_list

def predict_sentiment(comment_list):
    # Encode input
    encoded_list = encode_input(comment_list)
    # Predict sentiments
    predictions = np.argmax(model.predict(encoded_list), axis=-1)
    # Return sentiments
    sentiments = []
    for prediction in predictions:
        if prediction == 0:
            sentiments.append("Negative")
        elif prediction == 1:
            sentiments.append("Neutral")
        else:
            sentiments.append("Positive")
    return sentiments