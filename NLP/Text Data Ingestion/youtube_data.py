import os
from googleapiclient.discovery import build

api_key = 'AIzaSyAlADB91Hlfrnov9DrEYMMQ7u69HqtPYmk'
youtube = build('youtube', 'v3', developerKey=api_key)

search_query = 'Forex trading strategies'

search_response = youtube.videos().list(
    part='id,snippet',
    q=search_query,
    maxResults=5
).execute()

video_ids = [item['id']['videoId'] for item in search_response['items']]

# Iterate over each video ID to retrieve captions
for video_id in video_ids:
    captions_response = youtube.captions().list(
        part='id,snippet',
        videoId=video_id
    ).execute()

    # Check if captions are available for the video
    if captions_response['items']:
        caption_id = captions_response['items'][0]['id']['captionId']
        captions_get_response = youtube.captions().get(
            part='id,snippet',
            id=caption_id
        ).execute()

        transcript_text = captions_get_response['snippet']['textBody']
        print(transcript_text)
    else:
        print(f"No captions available for video ID {video_id}")