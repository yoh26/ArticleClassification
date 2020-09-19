import load_dataset as load
import preprocess

# load dataset
titles, categories = load.load_dataset('Dataset.txt')

assert len(titles) == len(categories), 'Not match each length'

tensor, config = preprocess.tokenize(titles)

# word and index mapping dictionaries
index_word = preprocess.convert_to_dict(config, 'index_word')
word_index = preprocess.convert_to_dict(config, 'word_index')

X_train, X_test, Y_train, Y_test = preprocess.split_dataset(tensor, categories)
