# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.start = ListNode(homepage)
       

    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.start
        self.start.next = node
        self.start = self.start.next

    def back(self, steps: int) -> str:

        while (steps and self.start.prev):
            self.start = self.start.prev
            steps -= 1
        return self.start.val

    def forward(self, steps: int) -> str:

        while(steps and self.start.next):
            self.start = self.start.next
            steps -= 1
        return self.start.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)