#!/usr/local/bin/python3.7
import config

# total number of words is 370103
def load_word(dictionary_index):
    dictionary_file = "words.txt"
    with open(dictionary_file) as fp:
        for i, line in enumerate(fp):
            if i == dictionary_index:
                word = line.strip()
    return word

def tweeter(client, text):
    try:
        tweet = client.update_status(text)
    except config.tweepy.TweepError:
        return None
    else:
        client.create_favorite(tweet.id)
    return

def lambda_handler(event, context):
    main()
    return

def main():

    client = config.login()
    dictionary_index = client.me().favourites_count

    try:
        word = load_word(dictionary_index)
    except UnboundLocalError: # out of bounds
        word = None
    
    if word:
        tweet_text = "imagine " + word
        tweeter(client, tweet_text)
        return

    else:
        # last message
        if dictionary_index == 370103:
            tweet_text = "imagine tweeting every word in the english language for a decade"
            tweeter(client, tweet_text)
        else:
            personal_account_id = int(config.os.getenv("PERSONAL_ACCOUNT_ID"))
            dm = "The decade's up!"
            client.send_direct_message(personal_account_id, dm)
        return

if __name__ == "__main__":
    main()
