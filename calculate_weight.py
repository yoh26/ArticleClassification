import load_dataset as load
import preprocess
import tensorflow as tf

# load dataset
titles, categories = load.load_dataset('Dataset.txt')

assert len(titles) == len(categories), 'Not match each length'

tensor, config = preprocess.tokenize(titles)

# split and shuffle dataset
X_train, X_test, Y_train, Y_test = preprocess.split_dataset(tensor, categories)

# make dataset pairs (title, category)
train_dataset = preprocess.concatenate_dataset(X_train, Y_train)
test_dataset = preprocess.concatenate_dataset(X_test, Y_test)

# split dataset to batches
BATCH_SIZE = 64
train_dataset = preprocess.to_batch(train_dataset, BATCH_SIZE)
test_dataset = preprocess.to_batch(test_dataset, BATCH_SIZE)

# word and index mapping dictionaries
index_word = preprocess.convert_to_dict(config, 'index_word')
word_index = preprocess.convert_to_dict(config, 'word_index')

'''
メモ
embeddingの引数は単語辞書の長さ
'''
s = input()
