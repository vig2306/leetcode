class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        two_house = 0
        one_house = nums[0]
        for index in range(1, n):

            take = nums[index] + two_house
            not_take = one_house

            two_house = one_house
            one_house = max(take, not_take)

        return one_house

    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [-1]*n
    #     dp[0] = nums[0]
    #     for index in range(1, n):
    #         if index - 2 < 0:
    #             take = nums[index]
    #         else:
    #             take = nums[index] + dp[index-2]

    #         not_take = dp[index-1]

    #         dp[index] = max(take, not_take)

    #     return dp[n-1]

    # def memoization(self, nums, index):
    #     if index < 0:
    #         return 0
    #     if index == 0:
    #         self.memo[index] = nums[index]
    #         return self.memo[index]
        
    #     if self.memo[index] != -1:
    #         return self.memo[index]
        
    #     take = nums[index] + self.memoization(nums, index - 2)
    #     not_take = self.memoization(nums, index-1)

    #     self.memo[index] = max(take, not_take)

    #     return max(take, not_take)
        

    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     self.memo = [-1]*(n)
    #     result = self.memoization(nums, n-1)
    #     return result

    # def recursion(self, nums, index):
    #     if index < 0:
    #         return 0
    #     if index == 0:
    #         return nums[index]
        
    #     take = nums[index] + self.recursion(nums, index - 2)
    #     not_take = self.recursion(nums, index-1)

    #     return max(take, not_take)
        

    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     result = self.recursion(nums, n-1)
    #     return result


        