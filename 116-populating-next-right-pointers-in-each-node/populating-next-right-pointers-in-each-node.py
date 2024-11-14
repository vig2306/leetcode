"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root

        #O(1) Space with two pointers;
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root

        # Once we reach the final level, we are done
        while leftmost.left:

            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the
            # corresponding links for the next level
            head = leftmost
            while head:

                # CONNECTION 1
                head.left.next = head.right

                # CONNECTION 2 (RIGHT CHILD OF NODE WITH LEFT CHILD OF NEXT NODE)
                if head.next:
                    head.right.next = head.next.left

                # Progress along the list (nodes on the current level)
                head = head.next

            # Move onto the next level
            leftmost = leftmost.left

        return root

        #O(N) Space with queue
        # queue = [root]

        # while queue:
        #     size = len(queue)
        #     for i in range(size):
        #         node = queue.pop(0)
        #         if i == size - 1:
        #             node.next = None
        #         else:
        #             node.next = queue[0]
                
        #         if node.left:
        #             queue.append(node.left)
                
        #         if node.right:
        #             queue.append(node.right)
        
        # return root
