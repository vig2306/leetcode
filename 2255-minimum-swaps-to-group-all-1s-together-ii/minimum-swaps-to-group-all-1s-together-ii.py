class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #O(n) Space
        #O(n) Time
        count_ones = sum(nums)
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])
        min_count_swaps = float('inf')
        i = 0
        j = count_ones
        # print(i,j)
        # start = 0
        curr_window_sum = sum(nums[i:j])
        count_swaps = count_ones - curr_window_sum
        min_count_swaps = min(count_swaps, min_count_swaps)
        j = j + 1
        
        for i in range(1, n):
            curr_window_sum = curr_window_sum - nums[i-1] + nums[j-1]
            # print(j, curr_window_sum)
            count_swaps = count_ones - curr_window_sum
            min_count_swaps = min(count_swaps, min_count_swaps)
            if min_count_swaps == 0:
                break
            # i = i+1
            j = j+1

        
        return min_count_swaps
            

        