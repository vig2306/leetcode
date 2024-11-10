# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # #Iterative
        # if root is None:
        #     return []
        # stack = []
        # result = []
        # curr = root
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     result.append(curr.val)
        #     curr = curr.right


        # return result


        #Recursive
        result = []
        def postorder(node, res):
            if node == None:
                return res
            
            
            res = postorder(node.left, res)
            res = postorder(node.right, res)
            res.append(node.val)

            return res
        
        result = postorder(root, [])
        return result
        
        