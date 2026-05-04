class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert word
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end_of_word = True

    # Search complete word
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end_of_word

    # Prefix search
    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# Main
trie = Trie()

trie.insert("cat")
trie.insert("car")
trie.insert("care")

print("Search cat:", trie.search("cat"))
print("Search dog:", trie.search("dog"))

print("Prefix ca:", trie.starts_with("ca"))
print("Prefix do:", trie.starts_with("do"))