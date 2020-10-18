import tensorflow as tf

class CModel():
    def __init__(self, vocab_size, hidden_units, final_output_units, dropout_rate, dense_layers, l2_rate):
        self.vocab_size = vocab_size + 1
        self.hidden_units = hidden_units
        self.final_output_units = final_output_units
        self.dropout_rate = dropout_rate
        self.dense_layers = dense_layers
        self.l2_rate = l2_rate

        # assemble model
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Embedding(self.vocab_size, self.hidden_units, mask_zero=True))
        model.add(tf.keras.layers.GlobalAveragePooling1D())
        model.add(tf.keras.layers.Dropout(self.dropout_rate))
        for _ in range(self.dense_layers):
            model.add(tf.keras.layers.Dense(self.hidden_units, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(self.l2_rate)))
            model.add(tf.keras.layers.Dropout(self.dropout_rate))
        model.add(tf.keras.layers.Dense(self.final_output_units, activation='softmax'))

        self.model = model

    def compile(self, learning_rate):
        self.learning_rate = learning_rate
        self.model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                           optimizer=tf.keras.optimizers.Adam(self.learning_rate),
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
