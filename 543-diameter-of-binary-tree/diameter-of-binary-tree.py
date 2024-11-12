# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node == None:
            return 0
        
        lh = self.dfs(node.left)
        rh = self.dfs(node.right)
        self.maxlen = max(self.maxlen, lh+rh)
        return max(lh,rh) +1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.maxlen = 0
        max_len = self.dfs(root)
        return self.maxlen

        
        