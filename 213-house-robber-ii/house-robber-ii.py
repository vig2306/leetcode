class Solution:
    #SPACE Optimised
    def tabulate(self, nums, isFirstTaken):
        n = len(nums)
        if isFirstTaken:
            two_house = 0
            one_house = nums[0]
            first_index = 1
            last_index = n - 2
        else:
            two_house = 0
            one_house = nums[1]
            first_index = 2
            last_index = n - 1

        for i in range(first_index, last_index+1):
            take = nums[i] + two_house
            not_take = one_house

            curr = max(take, not_take)
            two_house = one_house
            one_house = curr
        
        return one_house


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res1 = self.tabulate(nums, True)
        res2 = self.tabulate(nums, False)

        return max(res1, res2)

    # def tabulate(self, nums, dp):
    #     dp[0] = nums[0]
    #     n = len(nums)
    #     for i in range(1, n):
    #         take = nums[i]
    #         if i > 1:
    #             take += dp[i-2]
            
    #         not_take = dp[i-1]

    #         dp[i] = max(take, not_take)
        
    #     return dp[n-1]


    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     n = len(nums)
    #     dp1 = [-1]*(n-1)
    #     dp2 = [-1]*(n-1)

    #     res1 = self.tabulate(nums[:n-1], dp1)
    #     res2 = self.tabulate(nums[1:], dp2)

    #     return max(res1, res2)

    # def recursion(self, nums, index):
    #     if index < 0:
    #         return 0
        
    #     if index == 0:
    #         self.memo[index] = nums[index]
    #         return nums[index]
        
    #     if self.memo[index] != -1:
    #         return self.memo[index]

    #     take = nums[index] + self.recursion(nums, index-2)
    #     not_take= self.recursion(nums, index-1)

    #     self.memo[index] = max(take, not_take)

    #     return self.memo[index]

    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]
    #     n = len(nums)
    #     self.memo = [-1]*(n-1)
    #     res1 = self.recursion(nums[:n-1], n-2)
    #     self.memo = [-1]*(n-1)
    #     res2 = self.recursion(nums[1:], n-2)

    #     return max(res1, res2)

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
        