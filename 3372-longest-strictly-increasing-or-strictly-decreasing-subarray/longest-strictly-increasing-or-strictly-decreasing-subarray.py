class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxCount = 0
        increasingCount = 0
        decreasingCount = 0
        for i in range(len(nums)):
            if i == 0:
                increasingCount = 1
                decreasingCount = 1
            else:
                if nums[i] < nums[i-1]:
                    increasingCount = 1
                    decreasingCount += 1
                elif nums[i] > nums[i-1]:
                    increasingCount += 1
                    decreasingCount = 1
                else:
                    increasingCount = 1
                    decreasingCount = 1
            maxCount = max(maxCount, max(increasingCount, decreasingCount))
        
        return maxCount

        