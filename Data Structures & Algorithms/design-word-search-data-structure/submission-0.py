class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.kids = {}
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i, c in enumerate(word):
            if c not in cur.kids:
                cur.kids[c] = TrieNode()
            cur = cur.kids[c]
        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            curr = node
            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':
                    for kid in curr.kids.values():
                        if dfs(kid, i+1):
                            return True
                    return False
                if c not in curr.kids:
                    return False
                curr = curr.kids[c]
            return curr.endOfWord
                    
        return dfs(self.root, 0)
        
