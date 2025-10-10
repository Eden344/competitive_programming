# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or "" in strs:
            return ""
        root = TrieNode()
        
        
        for word in strs:
            curr = root
            for ch  in word:
                curr = curr.children[ch]
                
        curr.is_end = True

        ans = []
        for word in strs:
            ans.append(len(word))

        
        prefix = ""
        curr = root

        while len(curr.children) == 1 and not curr.is_end:
            ch = next(iter(curr.children))
            if len(prefix) < min(ans):
                prefix += ch
            curr= curr.children[ch]
        return prefix


        

