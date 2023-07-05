from flask_games import trie
import json

def get_dictionary() -> trie.Trie:
    dictionary = trie.Trie()
    # f = open('words_dictionary.json')
    # data = json.load(f)
    # for word in data.keys():
    #     word = word.strip()
    #     dictionary.insert(word)
    f = open('flask_games/dictionary.json')
    data = json.load(f)
    for word in data:
        word = word.strip()
        dictionary.insert(word)
    return dictionary

theTrie = get_dictionary()