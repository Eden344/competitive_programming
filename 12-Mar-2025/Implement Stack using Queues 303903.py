# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()
        

    def push(self, x: int) -> None:
        self.que1.append(x)
        

    def pop(self) -> int:
        if self.que1:
            return self.que1.pop()
        

    def top(self) -> int:
        return self.que1[-1]
        

    def empty(self) -> bool:
        if self.que1:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()