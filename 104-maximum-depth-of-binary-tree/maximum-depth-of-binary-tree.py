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


    def bfs(self, node, level):
        if node == None:
            return 0

        queue = [(node, level)]
        max_level = -1
        while queue:
            for i in range(len(queue)):
                curr_node, level = queue.pop(0)
                max_level = max(max_level, level)
                if curr_node.left:
                    queue.append((curr_node.left, level+1))
                if curr_node.right:
                    queue.append((curr_node.right,level+1))
        
        return max_level
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        # depth = self.dfs(root)
        depth = self.bfs(root, 0) + 1


        return depth

        