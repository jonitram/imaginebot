#!/usr/local/bin/python3.7
import config

# run every 4 hours

def get_recent_tweet(client):
    max_likes = None
    for tweet in client.user_timeline():
        if max_likes == None:
            max_likes = tweet
        elif tweet.favorite_count >= max_likes.favorite_count:
            max_likes = tweet
    return max_likes

def update_pin(client, tweet):
    personal_account_id = int(config.os.getenv("PERSONAL_ACCOUNT_ID"))
    status_update = "Most liked tweet update: \"" + tweet.text + "\" with: " + str(tweet.favorite_count) + " likes"
    client.send_direct_message(personal_account_id, status_update)
    return

def lambda_handler(event, context):
    main()
    return

def main():
    client = config.login()
    recent_liked = get_recent_tweet(client)
    if recent_liked:
        update_pin(client, recent_liked)
    return

if __name__ == "__main__":
    main()
