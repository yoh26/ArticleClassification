import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def read_dataset(filename):
    '''read dataset file
    
    # Argument
        filename = dataset file
        
    # Return
        dataset = a list of dataset
    '''
    with open(filename) as f:
        dataset = []
        for line in f:
            one_dataset = []
            line = line.strip('\n')
            index = line.rfind(' ')
            title = line[0:index]
            one_dataset.append(title)
            category = int(line[index:].strip(' '))
            one_dataset.append(category)
            dataset.append(one_dataset)
            
    return dataset

def clean_dataset(dataset):
    '''clean dataset
        1. remove duplication
        2. replace all numbers to 0
    
    # Argument
        dataset = a list of dataset
        
    # Returns
        a list of titles and categories
        title
        category
    '''
    # remove duplication by title
    df_dataset = pd.DataFrame(dataset, columns=['title', 'category'])
    df_dataset.drop_duplicates(subset='title', inplace=True)
    df_dataset.reset_index(drop=True, inplace=True)
    
    df_dataset['title'] = df_dataset['title'].str.lower()
    
    # replace all numbers to 0
    df_dataset['title'] = df_dataset['title'].replace('[0-9]', '0', regex=True)

    # remove single quotation
    df_dataset['title'] = df_dataset['title'].replace("'s", '', regex=True)
    df_dataset['title'] = df_dataset['title'].replace("'", '', regex=True)

    title = df_dataset['title'].to_numpy()
    category = df_dataset['category'].to_numpy()

    return title, category

def remove_stopwords(titles):
    '''remove stopwords from titles

    # Argument
    	titles = titles of dataset
        
    # Return
    	removed_stopwords_titles = titles of removing stopwords
    '''
    # get stopwords
    stop_words = set(stopwords.words('english'))

    removed_stopwords_titles = []

    # remove stopwords
    for title in titles:
        word_tokens = word_tokenize(title)
        removed_stopwords_title = [w for w in word_tokens if not w in stop_words]
        removed_stopwords_titles.append(' '.join(removed_stopwords_title))

    return removed_stopwords_titles

def load_dataset(filename):
    dataset = read_dataset(filename)
    titles, categories = clean_dataset(dataset)
    removed_stopwords_titles = remove_stopwords(titles)
    
    return removed_stopwords_titles, categories
