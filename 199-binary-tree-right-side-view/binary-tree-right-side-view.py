# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'Can be done both ways dfs, bfs'
class Solution:
    def dfs(self, node, level, res):
        if node == None:
            return res
        
        if level == len(res):
            res.append(node.val)
        
        res = self.dfs(node.right, level+1, res)
        res = self.dfs(node.left, level+1, res)

        return res


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        return self.dfs(root, 0, [])
        

        