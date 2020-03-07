#!/usr/local/bin/python3.8
import config
import pickle

# total number of words is 370103
def load_word(dictionary_index):
    dictionary_file = "words.txt"
    with open(dictionary_file) as fp:
        for i, line in enumerate(fp):
            if i == dictionary_index:
                word = line.strip()
    return word

def tweeter(client, word):
    tweet = "imagine " + word
    return client.update_status(tweet)

def main():

    index_file = ".dictionary_index.pickle"

    dictionary_index = config.load_pickle(index_file, 0)
    client = config.login()

    try:
        word = load_word(dictionary_index)
    except UnboundLocalError: # out of bounds
        word = None
    
    if word:
        tweet = tweeter(client, word)
        # like the tweet
        client.create_favorite(tweet.id)

        dictionary_index += 1
        config.save_pickle(index_file, dictionary_index)

        return

    else:
        # last message
        if dictionary_index == 370103:
            tweet_text = "imagine tweeting every word in the english language for a decade"
            tweet = client.update_status(tweet_text)

            client.create_favorite(tweet.id)

            dictionary_index += 1
            config.save_pickle(index_file, dictionary_index)
        else:
            personal_account_id = config.os.getenv("PERSONAL_ACCOUNT_ID")
            dm = "The decade's up!"
            client.send_direct_message(personal_account_id, dm)
        return

if __name__ == "__main__":
    main()
