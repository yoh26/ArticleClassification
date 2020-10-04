import tensorflow as tf
'''
googleの参考ページを参照して、モデルを構築する
'''

class CModel():
    def __init__(self, vocab_size, hidden_units):
        self.vocab_size = vocab_size + 1
        self.hidden_units = hidden_units

    def assemble(self):
        model = tf.keras.Sequential()
        # (batch_size, input_length) = (64, 1データの長さ)
        model.add(tf.keras.layers.Embedding(self.vocab_size, self.hidden_units))
        #model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(self.hidden_units)))
        #GlobalAveragePooling1Dのほうが性能よかった
        model.add(tf.keras.layers.GlobalAveragePooling1D())
        model.add(tf.keras.layers.Dense(self.hidden_units, activation='softmax'))
        model.add(tf.keras.layers.Dense(6))

        self.model = model

    def compile(self):
        self.model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                           optimizer=tf.keras.optimizers.Adam(1e-4),
                           metrics=['accuracy'])

    def fit(self, train_dataset, test_dataset):
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset

        history = self.model.fit(self.train_dataset, epochs=10,
                            validation_data=self.test_dataset,
                            validation_steps=30)

        self.history = history

        return self.history   

    def evaluate(self):
        test_loss, test_acc = self.model.evaluate(self.test_dataset)

        return test_loss, test_acc
