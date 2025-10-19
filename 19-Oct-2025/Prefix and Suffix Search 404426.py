# Problem: Prefix and Suffix Search - https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter:
    def __init__(self, words: List[str]):
        self.lookup = {}
        for idx, word in enumerate(words):
            n = len(word)
            for i in range(n+1):
                for j in range(n+1):
                    self.lookup[word[:i] + '#' + word[j:]] = idx

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get(pref + '#' + suff, -1)

        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)