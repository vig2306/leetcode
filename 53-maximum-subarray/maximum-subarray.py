class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0
        for i in range(len(nums)):
            # if curr_sum == 0:
                # start = i
            curr_sum = curr_sum + nums[i]
            if curr_sum >= max_sum:
                max_sum = curr_sum
                # ans_start = start
                # ans_end = i
            
            if curr_sum < 0:
                curr_sum = 0
            
        
        return max_sum
            

        

        