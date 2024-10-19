from text_preprocess import *

reddit_df['title'] = reddit_df['title'].apply(nltk.word_tokenize)
print(reddit_df)