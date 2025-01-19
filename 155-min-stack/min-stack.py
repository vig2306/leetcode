class MinStack:

    def __init__(self):
        self.stack = []
        # self.mini = float('inf')
        

    def push(self, val: int) -> None:
        mini = float('inf')
        if not self.stack:
            mini = val
        else:
            mini = self.stack[-1][1]
            mini = min(mini, val)
        self.stack.append((val, mini))
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()