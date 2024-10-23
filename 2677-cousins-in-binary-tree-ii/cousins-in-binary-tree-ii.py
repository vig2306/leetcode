# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bfs(self, root):
        if not root:
            return []

        result = []
        queue = [root]  # Initialize queue

        while queue:
            curr_sum = 0
            for i in range(len(queue)):
                node = queue.pop(0)
                curr_sum += node.val
                # result.append((node.val, level))

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(curr_sum)
        return result

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        level_sum = self.bfs(root)
        queue = [(root, root.val)]
        level = 0
        while len(queue) != 0:
            for i in range(len(queue)):

                node, value = queue.pop(0) 
                node.val = level_sum[level] - value
                child_sum = 0
                if node.left:
                    child_sum += node.left.val
                
                if node.right:
                    child_sum += node.right.val
                
                if node.left:
                    queue.append((node.left, child_sum))
                
                if node.right:
                    queue.append((node.right, child_sum))
            
            level+=1
        
        return root





        