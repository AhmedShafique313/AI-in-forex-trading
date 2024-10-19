from removal import *
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re

# tokenization and stopword removal
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

def preprocess_text(text):
    # Tokenization
    tokens = word_tokenize(text)
    
    # Stopword removal
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
    
    # Removal of special characters and punctuation
    cleaned_tokens = [re.sub(r'[^\w\s]', '', token) for token in stemmed_tokens]
    
    # Return the cleaned text as a string
    return ' '.join(cleaned_tokens)

reddit_df['processed_title'] = reddit_df['title'].apply(preprocess_text)
# reddit_df['processed_comments'] = reddit_df['comments'].apply(preprocess_text)
print(reddit_df[['title', 'processed_title']].head())