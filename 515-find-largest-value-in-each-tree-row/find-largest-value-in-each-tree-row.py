# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, depth):
        if not node:
            return

        if depth == len(self.result):
            self.result.append(node.val)
        else:
            self.result[depth] = max(self.result[depth], node.val)

        self.dfs(node.left, depth+1)
        self.dfs(node.right, depth+1)

        return 
         
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        self.result = []
        self.dfs(root, 0)

        return self.result


    #BFS
    # TC-> O(N)
    # SC -> O(N)
    # def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # if root is None:
        #     return []
        
        # queue = deque()
        # queue.append(root)
        # result = []
        # while queue:
        #     n = len(queue)
        #     max_val = float('-inf')
        #     for _ in range(n):
        #         node = queue.popleft()
        #         max_val = max(max_val, node.val)
        #         if node.left:
        #             queue.append(node.left)
                
        #         if node.right:
        #             queue.append(node.right)
            
        #     result.append(max_val)
        #     max_val = float('-inf')
        
        # return result

                

        