# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node1, node2):
        if node1 is None and node2 is not None:
            return False
        if node2 is None and node1 is not None:
            return False
        if node1 is None and node2 is None:
            return True
        
        if node1.val == node2.val:
            flag = True
        else:
            flag = False
        isLeft = self.dfs(node1.right, node2.left)
        isRight = self.dfs(node1.left, node2.right)

        return flag and (isLeft and isRight)


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        isSym = self.dfs(root, root)
        return isSym

        