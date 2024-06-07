class TrieNode:
    def __init__(self):
        self.next = {}
        self.isWord = False
        self.word = ""

    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.next:
                node.next[c] = TrieNode()
            node = node.next[c]
        node.isWord = True
        node.word = word

    def startsWith(self, word):
        node = self.root
        for c in word:
            if c not in node.next:
                return ""
            node = node.next[c]
            if node.isWord:
                return node.word
        return ""