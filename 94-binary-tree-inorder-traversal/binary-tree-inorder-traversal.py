# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # #Iterative
        # if root is None:
        #     return []
        # if root.left:
        #     stack = [root.left]
        # else:
        #     stack = [root]
        # result = []
        # while stack:
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        #     node = stack.pop()
        #     result.append(node.val)

        # return result


        #Recursive
        result = []
        def inorder(node, res):
            if node == None:
                return res
            
            
            res = inorder(node.left, res)
            res.append(node.val)
            res = inorder(node.right, res)

            return res
        
        result = inorder(root, [])
        return result
        