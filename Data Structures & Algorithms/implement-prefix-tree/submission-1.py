class TrieNode():
    def __init__(self, character = None, isFullWord = False):
        self.c = character
        self.isFullWord = isFullWord
        self.kids = {}
class PrefixTree:



    def __init__(self):
        self.root = TrieNode(None, False)

        

    def insert(self, word: str) -> None:
        currNode = self.root
        for i, c in enumerate(word):
            if c not in currNode.kids:
                currNode.kids[c] = TrieNode(c)
            currNode = currNode.kids[c]
        currNode.isFullWord = True
        



    def search(self, word: str) -> bool:
        currNode = self.root
        for i, c in enumerate(word):
            if c not in currNode.kids:
                return False
            currNode = currNode.kids[c]
        return currNode.isFullWord
        

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for i, c in enumerate(prefix):
            if c not in currNode.kids:
                return False
            currNode = currNode.kids[c]
        return True
        
        