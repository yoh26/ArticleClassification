from newsapi import NewsApiClient

# read apikey
apikey = ''
with open('newsapi_apikey.txt') as f:
    apikey = f.read().strip('\n')

newsapi = NewsApiClient(api_key=apikey)

# Category dictionary
categories_dict = {'business':'0',
                   'entertainment':'1',
                   'general':'2',
                   'health':'3',
                   'science':'4',
                   'sports':'5',
                   'technology':'6'}

# Create a news title dataset

# Get top headlines by each category
news_title_dataset = []
for category, category_num in categories_dict.items():
    top_headlines = newsapi.get_top_headlines(category=category,
                                              country='us',
                                              page_size=100)
    # [[title, category_num], ...]
    for article in top_headlines['articles']:
        one_title_dataset = []
        one_title_dataset.append(article['title'].strip(' '))
        one_title_dataset.append(category_num)
        news_title_dataset.append(one_title_dataset)

with open('Dataset.txt', mode='a') as f:
    for one_dataset in news_title_dataset:
        one_pair = ' '.join(one_dataset) + '\n'
        f.write(one_pair)

