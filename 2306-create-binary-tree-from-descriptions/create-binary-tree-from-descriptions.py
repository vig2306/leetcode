# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root = TreeNode()
        child_set = set()
        tree_map = {}
        for i in range(len(descriptions)):
            parent = descriptions[i][0]
            child = descriptions[i][1]
            isLeft = descriptions[i][2]
            child_set.add(child)
            tree_map[parent] = [None, None]
        
        for i in range(len(descriptions)):
            parent = descriptions[i][0]
            child = descriptions[i][1]
            isLeft = descriptions[i][2]
            if parent not in child_set:
                root.val = parent
            if isLeft:
                tree_map[parent][0] = child
            else:
                tree_map[parent][1] = child

            # tree_map[parent].append(child if isLeft else -child)
        print(root)
        print(tree_map)
        # del child_set
        def dfs(value):

            if not value:
                return
            if value not in tree_map:
                return TreeNode(value)
            
            
            node = TreeNode(value)
            node.left = dfs(tree_map[node.val][0])
            # print(node)
            node.right = dfs(tree_map[node.val][1])
            return node

        root = dfs(root.val)
        # def dfs(node):
        #     if node not in tree_map.keys():
        #         return root
        #     # print(root)
        #     node = TreeNode(root)
        #     node.left = dfs(TreeNode(tree_map[node.val][0]))
        #     node.right  = dfs(TreeNode(tree_map[root.val][1]))
        #     return root
        
        # root = dfs(root.val)



        # print(tree_map)
        return root
        