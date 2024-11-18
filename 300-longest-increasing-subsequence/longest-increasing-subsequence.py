class Solution:
    def __init__(self):
        self.memo = []

    def recur(self, nums, curr, prev_index):
        if curr == len(nums):
            return 0
        
        if self.memo[curr][prev_index+1] != -1:
            return self.memo[curr][prev_index+1]

        #Take
        take = 0
        if prev_index == -1 or nums[prev_index] < nums[curr]:
            take = 1 + self.recur(nums, curr+1, curr)

        #Not take
        notTake = 0 + self.recur(nums, curr+1, prev_index)

        self.memo[curr][prev_index+1] = max(take, notTake)
        return self.memo[curr][prev_index+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # DP table: +1 to handle the case when prev_index is -1
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Bottom-up calculation
        for curr in range(n - 1, -1, -1):
            for prev_index in range(curr - 1, -2, -1):  # Start from curr-1 to -1 for prev_index
                # Take case
                take = 0
                if prev_index == -1 or nums[prev_index] < nums[curr]:
                    take = 1 + dp[curr + 1][curr + 1]  # Shifted index for curr
                
                # Not take case
                not_take = dp[curr + 1][prev_index + 1]  # Shifted index for prev_index

                # Update DP table
                dp[curr][prev_index + 1] = max(take, not_take)

        # Result is the max LIS starting from index 0 with no previous element (-1 shifted to 0)
        return dp[0][0]

        
        for i in range(len(nums)):
            arr = []
            for j in range(len(nums)+1):
                arr.append(-1)
            self.memo.append(arr)
        ans = self.recur(nums, 0, -1)
        return ans
        