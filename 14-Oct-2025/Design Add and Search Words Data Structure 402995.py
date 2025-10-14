# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if  curr.children[index] is None:
                curr.children[index] =  TrieNode()
            curr = curr.children[index]
        curr.is_end = True
    
    

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i == len(word):
                return node.is_end
            c = word[i]

            if c == ".":
                for child in node.children:
                    if child and dfs(child, i + 1):
                        return True
                return False
            else:
                index = ord(c) - ord("a")
                child = node.children[index]
                if not child:
                    return False
                return dfs(child, i + 1)
        return dfs(self.root,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)