import tensorflow as tf
from sklearn.model_selection import train_test_split
import ast

def tokenize(titles):
    '''convert to sequences (integer)

    # Arguments
    	titles = titles of dataset

    # Returns
    	lists of sequences

    '''
    # initialize Tokenizer
    tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='', document_count=2)
    tokenizer.fit_on_texts(titles)

    # create tensor and padding
    tensor = tokenizer.texts_to_sequences(titles)
    tensor = tf.keras.preprocessing.sequence.pad_sequences(tensor, padding='post')

    config = tokenizer.get_config()

    return tensor, config

def split_dataset(tensor, categories):
    '''split dataset

    # Arguments
    	tensor = converted matrix from titles
        categories = categories of dataset

    # Returns
    	train and test dataset
    '''
    X_train, X_test, Y_train, Y_test = train_test_split(tensor, categories, train_size=0.8, random_state=42, shuffle=True)

    return X_train, X_test, Y_train, Y_test

def convert_to_dict(config, key):
    '''convert to dictionary from strings

    # Arguments
    	config = configuration of tokenizer
        key = key of configuration

    # Return
    	dictionary
    '''
    dictionary = ast.literal_eval(config[key])

    return dictionary
