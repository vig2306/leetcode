class Solution:
    def recursion(self, nums, index):
        if index < 0:
            return 0
        
        if index == 0:
            self.memo[index] = nums[index]
            return nums[index]
        
        if self.memo[index] != -1:
            return self.memo[index]

        take = nums[index] + self.recursion(nums, index-2)
        not_take= self.recursion(nums, index-1)

        self.memo[index] = max(take, not_take)

        return self.memo[index]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        self.memo = [-1]*(n-1)
        res1 = self.recursion(nums[:n-1], n-2)
        self.memo = [-1]*(n-1)
        res2 = self.recursion(nums[1:], n-2)

        return max(res1, res2)

    # def recursion(self, nums, index):
    #     if index < 0:
    #         return 0
        
    #     if index == 0:
    #         return nums[index]
        
    #     take = nums[index] + self.recursion(nums, index-2)
    #     not_take= self.recursion(nums, index-1)

    #     return max(take, not_take)

    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     res1 = self.recursion(nums[:n-1], n-2)
    #     res2 = self.recursion(nums[1:], n-2)

    #     return max(res1, res2)
        