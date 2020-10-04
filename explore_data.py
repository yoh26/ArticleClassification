import numpy as np
import matplotlib.pyplot as plt
import collections
import pandas as pd

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

def adjust_dataset_length(titles, labels):
    '''adjust dataset length to minimum label counts

    # Arguments
        titles: list, titles of dataset
        labels: lest, labels of dataset

    # Returns
        adjusted_titles: list
        adjusted_labels: list
    '''
    dataset = pd.DataFrame({'titles': titles,
                            'labels': labels
                            })
    # remove general news
    dataset = dataset[dataset.labels != 2]
    # remove duplications titles
    dataset.drop_duplicates(subset='titles', keep='first',inplace=True)

    # count labels
    label_counts = dataset['labels'].value_counts(ascending=True)

    minimum_label_counts = label_counts.iloc[0]

    np.random.seed(42)
    # choose same minimum_label_counts from each label
    l_0 = dataset[dataset.labels == 0].sample(n=minimum_label_counts)
    l_1 = dataset[dataset.labels == 1].sample(n=minimum_label_counts)
    l_3 = dataset[dataset.labels == 3].sample(n=minimum_label_counts)
    l_4 = dataset[dataset.labels == 4].sample(n=minimum_label_counts)
    l_5 = dataset[dataset.labels == 5].sample(n=minimum_label_counts)
    l_6 = dataset[dataset.labels == 6].sample(n=minimum_label_counts)

    dataset = pd.concat([l_0, l_1, l_3, l_4, l_5, l_6])
    dataset = dataset.reset_index(drop=True)

    adjusted_titles = dataset['titles'].values.tolist()
    adjusted_labels = dataset['labels'].values.tolist()

    return adjusted_titles, adjusted_labels
# function --------------------------------------------------------------

titles, labels = read_dataset('Dataset.txt')
#plot_title_length_distribution(titles, BINS)

#print_each_bin(titles, BINS)

# print each number of labels
#print(sorted(collections.Counter(labels).items()))
#plot_word_count_distribution(titles)
titles, labels = adjust_dataset_length(titles, labels)
