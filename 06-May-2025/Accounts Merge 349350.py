# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = {i: i for i in range(n)}
        size = [1 for _ in range(n)]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(i, j):
            pi = find(i)
            pj = find(j)
            if pi != pj:
                if size[pi] > size[pj]:
                    parent[pj] = pi
                    size[pi] += size[pj]
                else:
                    parent[pi] = pj
                    size[pj] += size[pi]

        email_idx = {}

       
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_idx:
                    union(i, email_idx[email])
                email_idx[email] = i

        
        idx = defaultdict(set)
        for email, i in email_idx.items():
            root = find(i)
            idx[root].add(email)

        
        result = []
        for i, emails in idx.items():
            name = accounts[i][0]
            result.append([name] + sorted(emails))

        return result
