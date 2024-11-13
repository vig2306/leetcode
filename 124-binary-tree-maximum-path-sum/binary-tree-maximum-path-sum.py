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
        
        leftSum = self.dfs(node.left)
        rightSum = self.dfs(node.right)

        if leftSum < 0:
            leftSum = 0
        if rightSum < 0:
            rightSum = 0
   
        currSum = leftSum + rightSum + node.val
        self.maxSum = max(self.maxSum, currSum)

        return max(leftSum, rightSum) + node.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        val = self.dfs(root)
        print(val)

        return self.maxSum
        