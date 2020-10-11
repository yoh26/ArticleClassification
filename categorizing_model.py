import tensorflow as tf

class CModel():
    def __init__(self, vocab_size, hidden_units, final_output_units):
        self.vocab_size = vocab_size + 1
        self.hidden_units = hidden_units
        self.final_output_units = final_output_units

    def assemble(self):
        model = tf.keras.Sequential()
        # (batch_size, input_length) = (64, 1データの長さ)
        model.add(tf.keras.layers.Embedding(self.vocab_size, self.hidden_units, mask_zero=True))
        #model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(self.hidden_units)))
        #GlobalAveragePooling1Dのほうが性能よかった
        model.add(tf.keras.layers.GlobalAveragePooling1D())
        model.add(tf.keras.layers.Dropout(0.2))
        model.add(tf.keras.layers.Dense(self.hidden_units, activation='relu'))
        model.add(tf.keras.layers.Dropout(0.2))
        model.add(tf.keras.layers.Dense(self.final_output_units, activation='softmax'))
        '''
        過学習している!!
        '''

        self.model = model

    def compile(self):
        self.model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                           optimizer=tf.keras.optimizers.Adam(1e-4),
                           metrics=['accuracy'])

    def fit(self, train_dataset, test_dataset, epochs):
        self.train_dataset = train_dataset
        self.test_dataset = test_dataset
        self.epochs = epochs

        history = self.model.fit(self.train_dataset, epochs=self.epochs,
                            validation_data=self.test_dataset,
                            validation_steps=30)

        self.history = history

        return self.history   

    def evaluate(self):
        test_loss, test_acc = self.model.evaluate(self.test_dataset)

        return test_loss, test_acc
