import load_dataset as load
import preprocess

# load dataset
titles, categories = load.load_dataset('Dataset.txt')

assert len(titles) == len(categories), 'Not match each length'

tensor = preprocess.tokenize(titles)

X_train, X_test, Y_train, Y_test = preprocess.split_dataset(tensor, categories)
