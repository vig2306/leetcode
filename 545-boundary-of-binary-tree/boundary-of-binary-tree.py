# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftBound(self, node):
        if node == None or node.left == None and node.right == None:
            return
        
        self.leftBoundary.append(node.val)
        if node.left:
            self.leftBound(node.left)
        else:
            self.leftBound(node.right)
        return
    
    def leafTraversal(self, node):
        if node == None:
            return
        if node.left == None and node.right == None:
            self.leaves.append(node.val)
            return
        
        self.leafTraversal(node.left)
        self.leafTraversal(node.right)
    
    def rightTraversal(self, node):
        if node == None or node.left == None and node.right == None:
            return
        
        if node.right:
            self.rightTraversal(node.right)
        else:
            self.rightTraversal(node.left)
        
        self.rightBoundary.append(node.val)
        


        

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        self.leftBoundary = [root.val]
        self.leaves = []
        self.rightBoundary = []
        self.leftBound(root.left)
        self.leafTraversal(root.left)
        self.leafTraversal(root.right)
        self.rightTraversal(root.right)
        
        res = []
        res = self.leftBoundary + self.leaves + self.rightBoundary

        return res

        