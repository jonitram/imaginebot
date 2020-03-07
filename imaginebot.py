#!/usr/local/bin/python3.7
import config
import pickle

index_file = ".dictionary_index.pickle"

dictionary_file = "words.txt"
# total number of words is 370103

def load_index():
    try:
        dictionary_index = pickle.load( open( index_file, "rb" ) )
    except (OSError, IOError):
        dictionary_index = 0
    return dictionary_index

def save_index(dictionary_index):
    pickle.dump( dictionary_index, open( index_file, "wb" ) )
    return

def load_word(dictionary_index):
    with open(dictionary_file) as fp:
        for i, line in enumerate(fp):
            if i == dictionary_index:
                word = line.strip()
    return word

def tweeter(client, word):
    tweet = "imagine " + word
    client.update_status(tweet)

    return

def main():

    dictionary_index = load_index()
    client = config.login()

    try:
        word = load_word(dictionary_index)
    except UnboundLocalError:
        word = None
    
    if word:

        tweeter(client, word)

        dictionary_index += 1
        save_index(dictionary_index)

        return

    else:
        # dont increase dictionary_index
        # bot is done
        return

if __name__ == "__main__":
    main()
