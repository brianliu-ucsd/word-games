class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        if self.contains(word):
            return
        # mark end of word
        word += "*"
        for letter in word:
            if letter not in trie:
                trie[letter] = {}
            trie = trie[letter]

    def contains(self, word: str) -> bool:
        trie = self.trie
        word += "*"
        for letter in word:
            if letter in trie:
                trie = trie[letter]
            else:
                return False
        return True

    def starts(self, prefix: str) -> bool:
        trie = self.trie
        for letter in prefix:
            if letter in trie:
                trie = trie[letter]
            else:
                return False
        return True