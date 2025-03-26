# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def back(store):

            if len(store) == n:
                res.append("".join(store))
                return



            back(store + ["0"])
            back(store + ["1"])

        back([])
        print(res)
        one = n//2
        ans = []

        for ch in res:
            if "00" not in ch:
                ans.append(ch)
        return ans

        