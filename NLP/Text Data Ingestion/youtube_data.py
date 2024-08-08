import requests
import json

# Set API key and search query
API_KEY = 'AIzaSyBvJhJlNcCGTiPJXNK-XsVDn5Hp_dw2Cyk'
QUERY = 'forex trading strategies OR market analysis OR economic news OR expert advisors'

# Set API endpoint and parameters for search
SEARCH_ENDPOINT = 'https://www.googleapis.com/youtube/v3/search'
SEARCH_PARAMS = {
    'key': API_KEY,
    'q': QUERY,
    'part': 'id,snippet',
    'maxResults': 50,
    'order': 'relevance'
}

# Send GET request to API endpoint for search
response = requests.get(SEARCH_ENDPOINT, params=SEARCH_PARAMS)

# Check if API returned an error
if response.status_code != 200:
    print(f'Error: {response.status_code}')
    exit()

# Parse JSON response
data = response.json()

# Extract video IDs from response
video_ids = [item['id']['videoId'] for item in data['items'] if item['id']['kind'] == 'youtube#video']

# Set API endpoint and parameters for videos.list
VIDEOS_ENDPOINT = 'https://www.googleapis.com/youtube/v3/videos'
VIDEOS_PARAMS = {
    'key': API_KEY,
    'id': ','.join(video_ids),
    'part': 'id,snippet'
}

# Send GET request to API endpoint for videos.list
response = requests.get(VIDEOS_ENDPOINT, params=VIDEOS_PARAMS)

# Check if API returned an error
if response.status_code != 200:
    print(f'Error: {response.status_code}')
    exit()

# Parse JSON response
data = response.json()

# Extract video IDs, titles, and descriptions from response
videos = []
for item in data['items']:
    video_id = item['id']
    title = item['snippet']['title']
    description = item['snippet']['description']
    videos.append({
        'video_id': video_id,
        'title': title,
        'description': description
    })

# Print search results
print('Search results:')
for video in videos:
    print(f"Video ID: {video['video_id']}, Title: {video['title']}, Description: {video['description']}")

# Save search results to a JSON file
with open('search_results.json', 'w') as f:
    json.dump(videos, f, indent=4)