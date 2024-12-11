class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        max_len = -1
        # count = 0
        nums.sort()
        left = 0
        right = 0
        while right <= len(nums):
            if right == len(nums) or nums[right] - nums[left] > 2*k:
                valid_window_size = right - left
                max_len = max(max_len, valid_window_size)
                left += 1
            

            right += 1
    
        
        return max_len







        