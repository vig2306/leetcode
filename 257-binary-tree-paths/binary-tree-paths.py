# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, res):
        if node is None:
            return 
        if not node.left and not node.right:
            res.append(node.val)
            self.ans.append(res[:])
            if res:
                res.pop()
            return
        res.append(node.val)
        self.dfs(node.left,res)
        self.dfs(node.right,res)
        res.pop()


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        self.dfs(root,[])
        result = []
        for path in (self.ans):
            temp = ""
            for i in range(len(path)):
                if i == len(path)-1:
                    temp = temp + str(path[i])
                    break
                temp = temp + str(path[i]) + "->"
            result.append(temp)

            
        return result



        