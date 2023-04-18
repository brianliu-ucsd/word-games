from trie import Trie
import json

def get_dictionary() -> Trie:
    dictionary = Trie()
    # f = open('words_dictionary.json')
    # data = json.load(f)
    # for word in data.keys():
    #     word = word.strip()
    #     dictionary.insert(word)
    f = open('dictionary.json')
    data = json.load(f)
    for word in data:
        word = word.strip()
        dictionary.insert(word)
    return dictionary

theTrie = get_dictionary()