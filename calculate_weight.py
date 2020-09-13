import clean_data as clean
import dist_repre as dist
import categorize_model as cmodel

# Load dataset
titles, categories = clean.cleanse_dataset('Dataset.txt')

titles = dist.remove_stopwords(titles)
