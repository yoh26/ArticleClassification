from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='54a128361b8149c2a6ba70193e3ddd65')

# Category dictionary
categories_dict = {'business':'0',
                   'entertainment':'1',
                   'general':'2',
                   'health':'3',
                   'science':'4',
                   'sports':'5',
                   'technology':'6'}

def create_news_title_dataset(newsapi, categories_dict, country='us', page_size=100):
    '''Create a news title dataset
    # Arguments
        newsapi: Instance of NewsApiClient
        categories_dict: Category dictionary {Category: Category_num}
        country: Country we want to get news
        page_size: The number of results to return per page
    # Returns
        a list of a news title dataset
    '''
    # Get top headlines by each category
    news_title_dataset = []
    for category, category_num in categories_dict.items():
        top_headlines = newsapi.get_top_headlines(category=category,
                                                  country=country,
                                                  page_size=page_size)
        # [[title, category_num], ...]
        for article in top_headlines['articles']:
            one_title_dataset = []
            one_title_dataset.append(article['title'].strip(' '))
            one_title_dataset.append(category_num)
            news_title_dataset.append(one_title_dataset)
    
    return news_title_dataset

news_title_dataset = create_news_title_dataset(newsapi, categories_dict)

def write_dataset(news_title_dataset):
    '''Write news_title_dataset to file
    # Argument
        a list of a news title dataset
    '''
    with open('Dataset.txt', mode='a') as f:
        for one_dataset in news_title_dataset:
            one_pair = ' '.join(one_dataset) + '\n'
            f.write(one_pair)

write_dataset(news_title_dataset)
