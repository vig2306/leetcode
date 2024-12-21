# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        queue = deque()
        queue.append((root, 0))
        res = []
        while queue:
            length = len(queue)
            temp = []
            for i in range(length):
                node, level = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
            
            if level%2 == 0:
                res.append(temp)
            else:
                res.append(temp[::-1])

        
        q = deque()
        q.append((root, 0))
        while q:
            length = len(q)
            j = 0
            for i in range(length):
                node, level = q.popleft()
                if level + 1 < len(res):
               
                    node.left.val = res[level+1][j]
                    node.right.val = res[level+1][j+1]
                    j += 2
                if node.left:
                    q.append((node.left, level+1))
                
                if node.right:
                    q.append((node.right, level+1))
        
        return root

                    
                    


        
        return root

                

        



        