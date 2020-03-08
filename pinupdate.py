#!/usr/local/bin/python3.7
import config

# run once a day

def get_recent_tweet(client):
    max_likes = None
    for tweet in client.user_timeline():
        if max_likes == None:
            max_likes = tweet
        elif tweet.favorite_count > max_likes.favorite_count:
            max_likes = tweet
    return max_likes

def get_last_tweet(client):
    for direct_message in client.list_direct_messages():
        if direct_message.user_id == int(config.os.getenv("PERSONAL_ACCOUNT_ID"))
            return direct_message.id

def update_pin(client, tweet, output_file):
    personal_account_id = int(config.os.getenv("PERSONAL_ACCOUNT_ID"))
    status_update = "New most liked tweet: \"" + tweet.text + "\" with: " + str(tweet.favorite_count) + " likes"
    client.send_direct_message(personal_account_id, status_update)
    return

def lambda_handler(event, context):
    main()
    return

def main():
    
    client = config.login()

    recent_liked = get_recent_tweet(client)

    return

if __name__ == "__main__":
    main()
