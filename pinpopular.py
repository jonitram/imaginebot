#!/usr/local/bin/python3.7
import config

# run every 8 hours

def get_recent_tweet(client):
    max_likes = None
    for tweet in client.user_timeline():
        if max_likes == None:
            max_likes = tweet
        elif tweet.favorite_count > max_likes.favorite_count:
            max_likes = tweet
    return max_likes

def update_pin(client, tweet, output_file):
    personal_account_id = int(config.os.getenv("PERSONAL_ACCOUNT_ID"))
    status_update = "New most liked tweet: \"" + tweet.text + "\" with: " + str(tweet.favorite_count) + " likes"
    client.send_direct_message(personal_account_id, status_update)
    config.save_pickle(output_file, tweet.id)
    return


def main():
    
    client = config.login()

    most_liked_file = ".most_liked_tweet.pickle"
    most_liked_tweet_id = config.load_pickle(most_liked_file, None)

    recent_liked = get_recent_tweet(client)

    if most_liked_tweet_id != None:
        # have a most liked tweet from before
        if recent_liked != None:
            # have recently liked tweet
            if recent_liked.favorite_count > client.get_status(id=most_liked_tweet_id).favorite_count:
                update_pin(client, recent_liked, most_liked_file)
    elif recent_liked != None:
        update_pin(client, recent_liked, most_liked_file)
    return

if __name__ == "__main__":
    main()
