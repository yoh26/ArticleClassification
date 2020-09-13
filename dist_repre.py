from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.models import word2vec

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
        removed_stopwords_titles.append(removed_stopwords_title)

    return removed_stopwords_titles

def get_dist_representations(titles):
    '''get distibuted representations

    # Argument
    	titles = titles of dataset

    # Return
    	model = vectors of words
    '''
    model = word2vec.Word2Vec(titles, size=200, min_count=3, window=5)
    return model
