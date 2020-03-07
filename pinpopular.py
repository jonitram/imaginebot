#!/usr/local/bin/python3.7
import config

# run every 8 hours

# return tweet
def get_recent_tweet(client):
    max_likes = None
    for tweet in client.user_timeline():
        if max_likes == None:
            max_likes = tweet
        elif tweet.favorite_count >= max_likes.favorite_count:
            max_likes = tweet
    return max_likes

def update_pin(client, tweet):
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
            if recent_liked.favorite_count >= client.get_status(id=most_liked_tweet_id).favorite_count:
                # new most_liked_tweet
                # dm to me
                # pickle it
            else:
                # comparison failed so don't send dm
        else:
            # do not have recently liked tweet so no comparison can be done
            # don't send dm
    elif recent_liked != None:
        # recently liked tweet is the new most_liked_tweet
        # send dm
        # pickle it
    return

if __name__ == "__main__":
    main()
