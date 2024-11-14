# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, val):
        if node == None:
            return None
        
        if val == node.val:
            return node
        
        if val < node.val:
            node = self.dfs(node.left, val)
        
        elif val > node.val:
            node = self.dfs(node.right, val)
        
        return node


    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = self.dfs(root, val)
        return node

        
        