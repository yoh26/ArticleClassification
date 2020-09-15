import tensorflow as tf
from sklearn.model_selection import train_test_split

def tokenize(titles):
    '''convert to sequences (integer)

    # Arguments
    	titles = titles of dataset

    # Returns
    	lists of sequences

    '''
    # initialize Tokenizer
    tokenizer = tf.keras.preprocessing.text.Tokenizer(filters='')
    tokenizer.fit_on_texts(titles)

    # create tensor and padding
    tensor = tokenizer.texts_to_sequences(titles)
    tensor = tf.keras.preprocessing.sequence.pad_sequences(tensor, padding='post')

    return tensor

def split_dataset(titles, categories):
    '''split dataset

    # Arguments
    	titles = titles of dataset
        categories = categories of dataset

    # Returns
    	train and test dataset
    '''
    X_train, X_test, Y_train, Y_test = train_test_split(titles, categories, train_size=0.8, random_state=42, shuffle=True)

    return X_train, X_test, Y_train, Y_test
