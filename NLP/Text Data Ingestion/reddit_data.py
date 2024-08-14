import praw
import json

reddit = praw.Reddit(
    client_id="9_KhWJ0ZPJnCUVDa5iVClw",
    client_secret="CYYiUFBNZrivlP0ig4v3j_IDt-PqoA",
    user_agent="Beneficial-Visit-507",
    username="scrapper",
)

subreddit = reddit.subreddit("Forex")
posts_data = []

for post in subreddit.top(time_filter="all", limit=100):
    post_data = {
        "title": post.title,
        "description": post.selftext,
        "url": post.url,
        "comments": []
    }

    for comment in post.comments:
        if isinstance(comment, praw.models.MoreComments):
            continue
        post_data["comments"].append(comment.body)

    posts_data.append(post_data)

# Save the post data to a JSON file
with open("forex_posts.json", "w") as f:
    json.dump(posts_data, f, indent=4)
