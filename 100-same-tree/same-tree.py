# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        left = self.dfs(p.left, q.left)
        right = self.dfs(p.right, q.right)
        return  left and right

    def bfs(self, p, q):
        queue1 = [p]
        queue2 = [q]
        flag = 0
        while queue1 and queue2:
            size1 = len(queue1)
            size2 = len(queue2)
            if size1 != size2:
                flag = 1
                break
            for i in range(size1):
                node1 = queue1.pop(0)
                node2 = queue2.pop(0)
                if node1.val != node2.val:
                    flag = 1
                    return False
                if node1.left and not node2.left or not node1.left and node2.left:
                    flag = 1 
                    return False
                else:
                    if node1.left and node2.left:
                        queue1.append(node1.left)
                        queue2.append(node2.left)
                if node1.right and not node2.right or not node1.right and node2.right:
                    flag = 1 
                    return False
                else:
                    if node1.right and node2.right:
                        queue1.append(node1.right)
                        queue2.append(node2.right)
                    
        if flag == 1:
            return False
        
        return True
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        val = self.dfs(p,q)
        return val
        # if p is None and q is None:
        #     return True
        # if p is None and q is not None or p is not None and q is None:
        #     return False
        # val = self.bfs(p,q)

        # return val

        