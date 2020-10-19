import numpy as np
import matplotlib.pyplot as plt
import collections
import pandas as pd

# function --------------------------------------------------------------

def read_dataset(filename):
    '''read dataset file

    # Argument
        filename: str, filename of dataset

    # Returns
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
    plt.xlabel('Length of a title')
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

def plot_word_count_distribution(titles):
    '''plots the word counts distribution

    # Argument
        titles: list, titles of dataset
    '''
    lower_titles = list(map(str.lower, titles))
    joined_titles = ' '.join(lower_titles)
    counter = collections.Counter(joined_titles.split())
    sorted_words = counter.most_common(30)

    words = []
    counts = []
    for count_pair in sorted_words:
        word, count = count_pair
        words.append(word)
        counts.append(count)

    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Counts')
    plt.title('Frequency distribution of words')
    plt.xticks(rotation=45)
    plt.show()

def print_tensor_length_distribution(tensor):
    '''print distribution of tensor length

    # Argument
        tensor: ndarray, numerical vectors
    '''
    # count words in each tensor
    tensor_length = [len(wc[wc != 0]) for wc in tensor]
    counter = collections.Counter(tensor_length)
    sorted_counter = counter.most_common(30)
    print(sorted_counter)

# function --------------------------------------------------------------

titles, labels = read_dataset('Dataset.txt')
#plot_title_length_distribution(titles, BINS)

#print_each_bin(titles, BINS)

# print each number of labels
#print(sorted(collections.Counter(labels).items()))

#plot_word_count_distribution(titles)
