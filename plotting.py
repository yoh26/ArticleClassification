import matplotlib.pyplot as plt

def plot_history(history):
    '''plot learning loss and accuracy history

    # Arguments
        history: History object
    '''
    history_dict = history.history

    acc = history_dict['accuracy']
    val_acc = history_dict['val_accuracy']
    loss = history_dict['loss']
    val_loss = history_dict['val_loss']
    
    epochs = range(1, len(acc) + 1)

    BLUE_DOT = 'bo'
    SOLID_BLUE_LINE = 'b'

    # plot training and validation loss
    # upper side
    plt.subplot(2, 1, 1)
    plt.plot(epochs, loss, BLUE_DOT, label='Training loss')
    plt.plot(epochs, val_loss, SOLID_BLUE_LINE, label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    
    # plot training and validation accuracy
    # lower side
    plt.subplot(2, 1, 2)
    plt.plot(epochs, acc, BLUE_DOT, label='Training acc')
    plt.plot(epochs, val_acc, SOLID_BLUE_LINE, label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.tight_layout()
    plt.show()
