# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()

        for word in words:
            curr = root
            for ch in word:
                curr = curr.children[ch]
            curr.is_end = True

        best = ""

        def dfs(node, path):
            nonlocal best
            if node != root and not node.is_end:
                return

            if len(path) > len(best) or (len(path) == len(best) and path < best):
                best = path

            for ch in sorted(node.children.keys()):
                dfs(node.children[ch], path + ch)

        dfs(root, "")
        return best
