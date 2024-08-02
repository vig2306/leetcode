class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #O(1) Space
        #O(n) Time
        count_ones = sum(nums)
        n = len(nums)
        # for i in range(n):
        #     nums.append(nums[i])
        min_count_swaps = float('inf')
        i = 0
        j = count_ones
        curr_window_sum = sum(nums[i:j])        
        for i in range(n):

            if i != 0:
                curr_window_sum = curr_window_sum - nums[i-1] + nums[j-1]
            # print(j)
            count_swaps = count_ones - curr_window_sum
            min_count_swaps = min(count_swaps, min_count_swaps)
            if min_count_swaps == 0:
                break
            j = j+1
            j = j % n

        
        return min_count_swaps
            

        