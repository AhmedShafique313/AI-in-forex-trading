import json
import pandas as pd

reddit_file_path = r'C:\Users\Ahmed Shafique\Documents\Projects\AI-in-forex-trading\NLP\Text Data Ingestion\reddit_posts.json'
youtube_file_path = r'C:\Users\Ahmed Shafique\Documents\Projects\AI-in-forex-trading\NLP\Text Data Ingestion\youtube_des.json'

with open(reddit_file_path) as O:
    reddit_data = json.load(O)

# with open(youtube_file_path) as O:
#     youtube_data = json.load(O)

reddit_df = pd.DataFrame(reddit_data)
# youtube_df = pd.DataFrame(youtube_data)

# remove missing rows
reddit_df = reddit_df.dropna()
# youtube_df = youtube_df.dropna()

# youtube_df = youtube_df.drop(columns= 'video_id')

print(reddit_df.head())
# print(youtube_df.head())