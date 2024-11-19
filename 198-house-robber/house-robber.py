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

        tabulate = [0]*(len(nums)+2)

        for index in range(len(nums)-1,-1,-1):

            take = nums[index] + tabulate[index+2]
            not_take = tabulate[index+1]

            tabulate[index] = max(take, not_take)
        
        return tabulate[0]

        self.memo = [-1]*(len(nums))
        return self.recursion(nums, 0)
        