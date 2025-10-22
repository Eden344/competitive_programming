# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class MapSum:

    def __init__(self):
        self.root = {}
        

    def insert(self, key: str, val: int) -> None:
        if key not in self.root:
            self.root[key] = val
        else:
            self.root[key] = val
        
        

    def sum(self, prefix: str) -> int:
        cnt = 0
        for key,val in self.root.items():
            if key.startswith(prefix):
                cnt += val
        return  cnt
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)