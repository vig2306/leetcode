# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node is None:
            return 0
        
        lh = self.dfs(node.left)
        rh = self.dfs(node.right)
        if lh == -1 or rh == -1:
            return -1
        if abs(lh-rh) > 1:
            return -1

        return max(lh, rh) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        val = self.dfs(root)
        if val == -1:
            return False
        
        return True
            
        