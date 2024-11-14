# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, preorder, bound):
        if self.pointer >= len(preorder) or preorder[self.pointer] > bound:
            return None
        
        root = TreeNode(preorder[self.pointer])
        self.pointer+=1
        root.left = self.dfs(preorder, root.val)
        root.right = self.dfs(preorder, bound)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.pointer = 0
        root = self.dfs(preorder, float('inf'))
        return root
        