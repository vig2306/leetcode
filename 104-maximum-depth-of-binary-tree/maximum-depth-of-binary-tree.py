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
        
        ldepth = self.dfs(node.left)
        rdepth = self.dfs(node.right)

        return max(ldepth, rdepth) + 1


    # def bfs(self)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        depth = self.dfs(root)

        return depth

        