import tensorflow as tf
from sklearn.model_selection import train_test_split
import ast

def tokenize(titles):
    '''convert to sequences (integer)

    # Arguments
    	titles = titles of dataset

    # Returns
        tensor:lists of sequences
        vocab_size: int, vocabulary size

    '''
    # initialize Tokenizer
    tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
    tokenizer.fit_on_texts(titles)

    # create tensor and padding
    tensor = tokenizer.texts_to_sequences(titles)
    tensor = tf.keras.preprocessing.sequence.pad_sequences(tensor, padding='post')

    # get vocabulary size
    config = tokenizer.get_config()
    index_to_word_dict = ast.literal_eval(config['index_word'])
    vocab_size = len(index_to_word_dict)

    return tensor, vocab_size

def split_dataset(tensor, labels):
    '''split dataset

    # Arguments
    	tensor = converted matrix from titles
        labels = list, labels of dataset

    # Returns
    	train and test dataset
    '''
    X_train, X_test, Y_train, Y_test = train_test_split(tensor, labels, train_size=0.8, random_state=42, shuffle=True)

    return X_train, X_test, Y_train, Y_test
