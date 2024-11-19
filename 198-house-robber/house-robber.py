class Solution:
    def recursion(self, nums, index):
        if index >= len(nums):
            return 0
        
        if self.memo[index] != -1:
            return self.memo[index]
        
        take = nums[index] + self.recursion(nums, index+2)
        not_take = self.recursion(nums, index+1)

        self.memo[index] = max(take, not_take)

        return self.memo[index]

    def rob(self, nums: List[int]) -> int:
        self.memo = [-1]*(len(nums))
        return self.recursion(nums, 0)
        