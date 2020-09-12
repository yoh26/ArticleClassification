import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# stopwordの削除
def remove_stopwords(titles):
    '''
    '''
    stop_words = set(stopwords.words('english'))
    removed_stopwords_titles = []
    for title in titles:
        word_tokens = word_tokenize(title)
        removed_stopwords_titles = [w for w in word_tokens if not w in stop_words]

    return removed_stopwords_titles

