import json
import pandas as pd
import re

reddit_file_path = r'C:\Users\Ahmed Shafique\Documents\Projects\AI-in-forex-trading\NLP\Text Data Ingestion\reddit_posts.json'
youtube_file_path = r'C:\Users\Ahmed Shafique\Documents\Projects\AI-in-forex-trading\NLP\Text Data Ingestion\youtube_des.json'

with open(reddit_file_path, encoding='utf-8') as O:
    reddit_data = json.load(O)

with open(youtube_file_path, encoding='utf-8') as O:
    youtube_data = json.load(O)

reddit_df = pd.DataFrame(reddit_data)
youtube_df = pd.DataFrame(youtube_data)

# remove missing rows
reddit_df = reddit_df.dropna()
youtube_df = youtube_df.dropna()

# youtube_df = youtube_df.drop(columns= 'video_id')

# emojies category
def remove_emojis(text):
    # Regex pattern for matching emojis
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U00002702-\U000027B0"  # Dingbats
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)

reddit_df['title'] = reddit_df['title'].apply(remove_emojis)
reddit_df['comments'] = reddit_df['comments'].apply(remove_emojis)
youtube_df['title'] = youtube_df['title'].apply(remove_emojis)
youtube_df['description'] = youtube_df['description'].apply(remove_emojis)

print(reddit_df.head())
print(youtube_df.head())