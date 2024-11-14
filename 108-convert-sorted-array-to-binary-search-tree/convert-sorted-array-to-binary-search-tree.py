# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, l, r, nums):
        if l > r:
            return None
        
        mid = (l+r) // 2
        root = TreeNode(nums[mid])
        root.left = self.dfs(l,mid-1,nums)
        root.right = self.dfs(mid+1, r, nums)

        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        return self.dfs(0, len(nums)-1, nums)
        