class MyStack:

    def __init__(self):
        self.queue = deque()
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        length = len(self.queue)
        while length > 1:
            val = self.queue.popleft()
            self.queue.append(val)
            length -= 1

        

    def pop(self) -> int:
        val = -1
        if self.queue:
            val = self.queue.popleft()
        return val

    def top(self) -> int:
        val = -1
        if self.queue:
            val = self.queue[0]
        
        return val

    def empty(self) -> bool:
        if self.queue:
            return False
        
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()