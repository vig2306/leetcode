class ListNode:
    def __init__(self, val, nextNode, prevNode):
        self.val = val
        self.nextNode = nextNode
        self.prevNode = prevNode

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.nextNode = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        cur = ListNode(value, self.right, self.right.prevNode)
        self.right.prevNode.nextNode = cur
        self.right.prevNode = cur
        self.space -= 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.left.nextNode = self.left.nextNode.nextNode
        self.left.nextNode.prevNode = self.left
        self.space += 1

        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.left.nextNode.val
        

    def Rear(self) -> int:

        if self.isEmpty():
            return -1
        
        return self.right.prevNode.val
        

    def isEmpty(self) -> bool:
        if self.left.nextNode == self.right:
            return True
        
        return False
        
    def isFull(self) -> bool:
        if self.space == 0:
            return True
        
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()