import json
import pandas as pd

reddit_file_path = r'C:\Users\Ahmed Shafique\Documents\Projects\AI-in-forex-trading\NLP\Text Data Ingestion\reddit_posts.json'
youtube_file_path = r'C:\Users\Ahmed Shafique\Documents\Projects\AI-in-forex-trading\NLP\Text Data Ingestion\youtube_des.json'

with open(reddit_file_path) as O:
    reddit_data = json.load(O)


reddit_df = pd.DataFrame(reddit_data)


# remove missing rows
reddit_df = reddit_df.dropna()

reddit_df['title'] = reddit_df['title'].str.lower()
print(reddit_df.head())
