class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
        

    def push(self, x: int) -> None:
        if len(self.q1) == 0:
            self.q1.append(x)
        else:
            num = self.q1.pop()
            self.q2.append(num)
            self.q1.append(x)
        
    def pop(self) -> int:
        # if len(self.q1) == 0:
        #     return -1

        top_num = self.q1.pop()
        if len(self.q2) > 0:
            self.q1.append(self.q2.pop())
        return top_num

    def top(self) -> int:
        # if len(self.q1) == 0:
        #     return -1
        top_num = self.q1[0]
        return top_num
        
    def empty(self) -> bool:
        if not self.q1 and not self.q2:
            return True
        return False

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()