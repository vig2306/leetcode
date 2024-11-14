# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, k):
        if node == None or self.pointer > k:
            return
        
        self.dfs(node.left, k)
        self.pointer += 1
        if self.pointer == k:
            self.ans = node.val
            return
        self.dfs(node.right, k)

        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = -1
        self.pointer = 0
        self.dfs(root, k)
        return self.ans
        