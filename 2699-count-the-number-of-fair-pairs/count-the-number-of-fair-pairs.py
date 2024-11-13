class Solution:
    def bin_search(self, nums, l, r, target):
        while l<=r:
            m = (l+r) // 2
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1
        return r
            

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            # X + nums[i] < upper:
            # Y + nums[i] < lower:
            # We find two elements X & Y such that we find the max possible value which is lesser than the Upper
            # We find the max possible element which is lesser than the lower that is the first element which can be considered in lower
            # We need to find index so doing binary search
            
            low_target = lower - nums[i]
            upper_target = upper - nums[i] + 1 #Do +1 to include 6 and keep the logic of binary search as same

            up_binary_index = self.bin_search(nums, i+1, len(nums) - 1, upper_target)
            low_binary_index = self.bin_search(nums, i+1, len(nums) - 1, low_target)

            ans += up_binary_index - low_binary_index
        
        return ans

            

