class Solution:
    def recursion(self, nums, subset, index):
        if index == len(nums):
            self.result.append(subset.copy())
            return
        subset.append(nums[index])
        self.recursion(nums, subset, index+1)
        subset.pop()
        self.recursion(nums, subset, index+1)

        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.recursion(nums, [], 0)
        return self.result
        