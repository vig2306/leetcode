# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, level):
        if not node:
            return 0
        
        if node.val not in self.node_level:
            self.node_level[node.val] = level

        hl =  self.dfs(node.left, level + 1)
        hr = self.dfs(node.right, level + 1)

        self.bottom_up_height[node.val] = max(hr, hl)
        if level not in self.level_max_bottom_height_mapping:
            self.level_max_bottom_height_mapping[level] = [max(hr,hl)]
            heapq.heapify(self.level_max_bottom_height_mapping[level])
    
        else:
            heapq.heappush(self.level_max_bottom_height_mapping[level],(max(hr,hl)))
            if len(self.level_max_bottom_height_mapping[level]) > 2:
                heapq.heappop(self.level_max_bottom_height_mapping[level])

        
        return max(hr, hl) + 1
        

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.node_level = {}
        self.bottom_up_height = {}
        self.level_max_bottom_height_mapping = {}

        self.dfs(root, 0)

        # print(self.node_level)
        # print(self.bottom_up_height, self.level_max_bottom_height_mapping)

        ans = []
        for q in queries:
            level_current_node = self.node_level[q]
            max_values_at_level = self.level_max_bottom_height_mapping[level_current_node]
            if len(max_values_at_level) == 1: # only 1 node to remove at current level which max itself
                ans.append(level_current_node - 1)
            elif max_values_at_level[-1] == self.bottom_up_height[q]:
                ans.append(max_values_at_level[0] + level_current_node)
            else:
                ans.append(max_values_at_level[-1] + level_current_node)
            
        return ans