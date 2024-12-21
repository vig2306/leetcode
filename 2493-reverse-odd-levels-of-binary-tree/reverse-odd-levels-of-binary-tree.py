# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, left_child, right_child, level):
        if left_child is None or right_child is None:
            return
        
        if level%2 != 0:
            left_child.val, right_child.val = right_child.val, left_child.val
        
        self.dfs(left_child.left, right_child.right, level+1)
        self.dfs(left_child.right, right_child.left, level+1)

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root.left, root.right, 1)
        
        return root
        

    #BFS Solution Single Pass:
    #TC: O(2N)
    #SC: O(N)

    # def reverseOddLevels(self, root):
    #     if not root:
    #         return None  # Return None if the tree is empty.

    #     queue = [root]  # Start BFS with the root node.
    #     level = 0

    #     while queue:
    #         size = len(queue)
    #         current_level_nodes = []

    #         # Process all nodes at the current level.
    #         for _ in range(size):
    #             node = queue.pop(0)
    #             current_level_nodes.append(node)

    #             if node.left:
    #                 queue.append(node.left)
    #             if node.right:
    #                 queue.append(node.right)

    #         # Reverse node values if the current level is odd.
    #         if level % 2 == 1:
    #             left, right = 0, len(current_level_nodes) - 1
    #             while left < right:
    #                 tmp = current_level_nodes[left].val
    #                 current_level_nodes[left].val = current_level_nodes[
    #                     right
    #                 ].val
    #                 current_level_nodes[right].val = tmp
    #                 left += 1
    #                 right -= 1

    #         level += 1

    #     return root  # Return the modified tree root.

    #BFS Solution with Extra iteration to build tree
    #TC: O(2N)
    #SC: O(N)
    # def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if root is None:
    #         return root
    #     queue = deque()
    #     queue.append((root, 0))
    #     res = []
    #     while queue:
    #         length = len(queue)
    #         temp = []
    #         for i in range(length):
    #             node, level = queue.popleft()
    #             temp.append(node.val)
    #             if node.left:
    #                 queue.append((node.left, level + 1))
    #             if node.right:
    #                 queue.append((node.right, level + 1))
            
    #         if level%2 == 0:
    #             res.append(temp)
    #         else:
    #             res.append(temp[::-1])

        
    #     q = deque()
    #     q.append((root, 0))
    #     while q:
    #         length = len(q)
    #         j = 0
    #         for i in range(length):
    #             node, level = q.popleft()
    #             if level + 1 < len(res):
               
    #                 node.left.val = res[level+1][j]
    #                 node.right.val = res[level+1][j+1]
    #                 j += 2
    #             if node.left:
    #                 q.append((node.left, level+1))
                
    #             if node.right:
    #                 q.append((node.right, level+1))
        
    #     return root