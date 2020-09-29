import numpy as np
import matplotlib.pyplot as plt

def read_dataset(filename):
    '''read dataset file

    # Argument
        filename: str, filename of dataset

    # Return
        titles: list, titles of dataset
        labels: list, categories of titles
    '''
    titles = []
    labels = []
    with open(filename) as f:
        for line in f:
            line = line.strip('\n')
            index = line.rfind(' ')
            title = line[0:index]
            titles.append(title)

            label = int(line[index:].strip(' '))
            labels.append(label)

    return titles, labels

def plot_title_length_distribution(titles):
    '''plots the title length distribution

    # Argument
        titles: list, titles of dataset
    '''
    plt.hist([len(s.split()) for s in titles], bins=40)
    plt.xlabel('length of a title')
    plt.ylabel('Number of titles')
    plt.title('Title length distribution')
    plt.show()


titles, labels = read_dataset('Dataset.txt')
plot_title_length_distribution(titles)
