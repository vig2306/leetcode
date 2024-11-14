# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def search(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.search(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.search(root.right, p ,q)
        else:
            return root



    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        node = self.search(root,p,q)

        return node

