import numpy as np
import pandas as pd
import collections
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

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

def remove_stopwords(dataset):
    '''remove stopwords from titles

    # Argument
        dataset = Dataflame, titles and labels

    # Return
        dataset = Dataflame, titles and labels
    '''
    # get stopwords
    stop_words = set(stopwords.words('english'))

    removed_stopwords_titles = []
    removed_stopwords_labels = []

    # remove stopwords
    titles = dataset['titles'].to_list()
    labels = dataset['labels'].to_list()
    for title, label in zip(titles, labels):
        word_tokens = word_tokenize(title)
        removed_stopwords_title = [w for w in word_tokens if not w in stop_words]
        removed_stopwords_titles.append(' '.join(removed_stopwords_title))
        removed_stopwords_labels.append(label)

    removed_stopwords_dataset = pd.DataFrame({'titles': removed_stopwords_titles,
                                              'labels': removed_stopwords_labels
                                             })

    removed_stopwords_dataset.dropna(inplace=True)

    return removed_stopwords_dataset

def remove_health_data(dataset):
    '''
    healthデータが他のデータに比べて少ないのでhealthデータを削除して学習してみる
    '''
    dataset = dataset[dataset.labels != 3]
    # dataset.replace({'labels': {4:3}}, inplace=True)
    # dataset.replace({'labels': {5:4}}, inplace=True)
    dataset = dataset.replace({'labels': {4:3}})
    dataset = dataset.replace({'labels': {5:4}})

    return dataset

def load_dataset(filename):
    dataset = read_dataset(filename)

    # remove duplication by title
    dataset.drop_duplicates(subset='titles', keep='first',inplace=True)

    # remove "'s"
    dataset['titles'] = dataset['titles'].replace("'s", '', regex=True)
    
    # remove punctuations
    dataset['titles'] = dataset['titles'].str.translate(str.maketrans( '', '',string.punctuation + "’‘"))

    # to lowercase
    dataset['titles'] = dataset['titles'].str.lower()

    # replace all numbers to 0
    dataset['titles'] = dataset['titles'].replace('[0-9]', '0', regex=True)

    # remove stopwords
    dataset = remove_stopwords(dataset)

    # remove over max length titles
    MAX_LEN = 20
    dataset = dataset[dataset.titles.str.split().str.len() <= MAX_LEN]

    #dataset = remove_health_data(dataset)

    return dataset
