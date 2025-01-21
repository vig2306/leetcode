class TreeNode():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class MyCalendar:
    def __init__(self):
        self.root = None
        

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = TreeNode(startTime, endTime)
            return True
        
        return self.insert(startTime, endTime, self.root)
    
    def insert(self, startTime, endTime, node):
        while True:
            if startTime >= node.end:
                if not node.right:
                    node.right = TreeNode(startTime, endTime)
                    return True
                
                node = node.right
            
            elif endTime <= node.start:
                if not node.left:
                    node.left = TreeNode(startTime, endTime)
                    return True
                node = node.left
            else:
                return False
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)