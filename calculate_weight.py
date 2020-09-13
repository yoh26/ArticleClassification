import clean_data as clean
import dist_repre as dist

# Load dataset
titles, categories = clean.cleanse_dataset('Dataset.txt')

titles = dist.remove_stopwords(titles)

assert len(titles) == len(categories), 'Not match dataset'

# Get distributed representations 
model = dist.get_dist_representations(titles)
