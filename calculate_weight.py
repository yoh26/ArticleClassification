import tensorflow as tf
import load_dataset as load
import preprocess
from categorizing_model import CModel

# load dataset
titles, categories = load.load_dataset('Dataset.txt')

assert len(titles) == len(categories), 'Not match each length'

tensor, config = preprocess.tokenize(titles)

# split and shuffle dataset
X_train, X_test, Y_train, Y_test = preprocess.split_dataset(tensor, categories)

# make dataset pairs (title, category)
train_dataset = tf.data.Dataset.from_tensor_slices((X_train, Y_train))
test_dataset = tf.data.Dataset.from_tensor_slices((X_test, Y_test))

# split dataset to batches
BATCH_SIZE = 64
train_dataset = train_dataset.batch(BATCH_SIZE)
test_dataset = test_dataset.batch(BATCH_SIZE)

# word and index mapping dictionaries
index_word = preprocess.convert_to_dict(config, 'index_word')
word_index = preprocess.convert_to_dict(config, 'word_index')

model = CModel(len(index_word), 64)
model.assemble()
model.compile()
history = model.fit(train_dataset, test_dataset)
test_loss, test_acc = model.evaluate()
print(test_loss)
print(test_acc)

s = input()
