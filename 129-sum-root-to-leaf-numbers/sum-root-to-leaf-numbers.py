# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, result):
        if root is None:
            return 0
        
        result = result*10 + root.val

        if root.left is None and root.right is None:
            return result
            
        resleft = self.dfs(root.left, result)
        resright = self.dfs(root.right, result)

        return resleft + resright

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sol = self.dfs(root, 0)

        return sol

        