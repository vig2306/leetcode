class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.currTotal = 0
        

    def next(self, val: int) -> float:
        self.currTotal += val
        self.queue.append(val)
        if len(self.queue) > self.size:
            remove = self.queue.popleft()
            self.currTotal -= remove
        
        return self.currTotal/len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)