# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result


        # #Recursive
        # result = []
        # def preorder(node, res):
        #     if node == None:
        #         return res
            
        #     res.append(node.val)
        #     res = preorder(node.left, res)
        #     res = preorder(node.right, res)

        #     return res
        
        # result = preorder(root, [])
        # return result


            
            


        