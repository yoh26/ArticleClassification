import pandas as pd

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
    
    title = df_dataset['title'].to_numpy()
    category = df_dataset['category'].to_numpy()

    return title, category

def cleanse_dataset(filename):
    dataset = read_dataset(filename)
    title, category = clean_dataset(dataset)
    
    return title, category
