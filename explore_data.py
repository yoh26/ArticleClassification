import numpy as np
import matplotlib.pyplot as plt

# function --------------------------------------------------------------

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

BINS = 40

def plot_title_length_distribution(titles, bins):
    '''plots the title length distribution

    # Arguments
        titles: list, titles of dataset
        bins: int, number of bins
    '''
    plt.hist([len(s.split()) for s in titles], bins=bins)
    plt.xlabel('length of a title')
    plt.ylabel('Number of titles')
    plt.title('Title length distribution')
    plt.show()

def print_each_bin(titles, bins):
    '''print the values of the histogram

    # Arguments
        titles: list, titles of dataset
        bins: int, number of bins
    '''
    hists, _ = np.histogram([len(s.split()) for s in titles], bins=bins)
    for index, hist in enumerate(hists):
        print('length of a title {0}: {1}'.format(index + 1, hist))

# function --------------------------------------------------------------

titles, labels = read_dataset('Dataset.txt')

#plot_title_length_distribution(titles, BINS)

#print_each_bin(titles, BINS)
