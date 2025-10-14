# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}


class Solution:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True
                
    
    def startsWith(self, word: str) -> bool:
        curr = self.root
        prefix = ""
        for c in word:
            
            if c not in curr.children:
                break
            curr = curr.children[c]
            prefix +=c
            if curr.is_end:
                return prefix
        return word
    

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        for word in dictionary:
            self.insert(word)
        words = sentence.split()
        replace = [self.startsWith(word) for word in words]
        return " ".join(replace)


        