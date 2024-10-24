# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 and node2 or node1 and not node2:
            return False
        if node1.val != node2.val:
            return False
        
        result1 = self.dfs(node1.left, node2.left) and self.dfs(node1.right, node2.right)
        result2 = self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.left)

        return result1 or result2
    

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        result = False
        if not root1 and not root2:
            return True
        if root1 and root2:
            if root1.val != root2.val:
                return False
            result = self.dfs(root1, root2)
        
        return result


        