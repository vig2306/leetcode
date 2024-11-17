class Solution:
    def recursion(self, nums, subset, index):
        if index == len(nums):
            sub_tup = tuple(sorted(subset))
            self.result.add(sub_tup)
            # self.result.append(subset.copy())
            return
        subset.append(nums[index])
        self.recursion(nums, subset, index+1)
        subset.pop()
        self.recursion(nums, subset, index+1)

        return

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = set()
        self.recursion(nums, [], 0)
    
        return sorted(list(self.result))
        
        