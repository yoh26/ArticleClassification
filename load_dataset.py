import numpy as np
import pandas as pd
import collections
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def read_dataset(filename):
    '''read dataset file

    # Argument
        filename: str, filename of dataset

    # Return
        dataset: Dataflame, titles and labels
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

    dataset = pd.DataFrame({'titles': titles,
                            'labels': labels
                            })
    return dataset

def adjust_dataset_length(dataset):
    '''adjust dataset length to minimum label counts

    # Arguments
        dataset: Dataflame, titles and labels

    # Returns
        adjusted_dataset: Dataflame, titles adn labels
    '''
    # count labels
    label_counts = dataset['labels'].value_counts(ascending=True)

    minimum_label_counts = label_counts.iloc[0]

    # set the seed
    np.random.seed(42)

    # choose same minimum_label_counts from each label
    l_0 = dataset[dataset.labels == 0].sample(n=minimum_label_counts)
    l_1 = dataset[dataset.labels == 1].sample(n=minimum_label_counts)
    l_2 = dataset[dataset.labels == 2].sample(n=minimum_label_counts)
    l_3 = dataset[dataset.labels == 3].sample(n=minimum_label_counts)
    l_4 = dataset[dataset.labels == 4].sample(n=minimum_label_counts)
    l_5 = dataset[dataset.labels == 5].sample(n=minimum_label_counts)

    adjusted_dataset = pd.concat([l_0, l_1, l_2, l_3, l_4, l_5])

    return adjusted_dataset

def remove_stopwords(dataset):
    '''remove stopwords from titles

    # Argument
        dataset = Dataflame, titles and labels
    '''
    # get stopwords
    stop_words = set(stopwords.words('english'))

    removed_stopwords_titles = []

    # remove stopwords
    titles = dataset['titles'].to_list()
    for title in titles:
        word_tokens = word_tokenize(title)
        removed_stopwords_title = [w for w in word_tokens if not w in stop_words]
        removed_stopwords_titles.append(' '.join(removed_stopwords_title))

    dataset['titles'] = pd.Series(removed_stopwords_titles)

    dataset.dropna(inplace=True)

def load_dataset(filename):
    dataset = read_dataset(filename)

    # remove duplication by title
    dataset.drop_duplicates(subset='titles', keep='first',inplace=True)

    # adjust each label to be same length
    dataset = adjust_dataset_length(dataset)

    # to lowercase
    dataset['titles'] = dataset['titles'].str.lower()

    # replace all numbers to 0
    dataset['titles'] = dataset['titles'].replace('[0-9]', '0', regex=True)

    # remove stopwords
    remove_stopwords(dataset)

    return dataset
