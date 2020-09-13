from sklearn.model_selection import train_test_split
'''
ToDo
1. データを分割する
2. モデル作成
'''

def split_dataset(titles, categories):
    '''split dataset

    # Arguments
    	titles = titles of dataset
        categories = categories of dataset

    # Returns
    	train and test dataset
    '''
    X_train, X_test, Y_train, Y_test = train_test_split(titles, categories, train_size=0.8, random_state=42, shuffle=True)

    return X_train, X_test, Y_train, Y_test
