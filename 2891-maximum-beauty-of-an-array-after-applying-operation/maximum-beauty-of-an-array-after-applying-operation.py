class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        #Line Sweep
        start = []
        end = []
        max_len = 0
        for i in range(len(nums)):
            mini = nums[i] - k
            maxi = nums[i] + k
            start.append(mini)
            end.append(maxi)
        
        start.sort()
        end.sort()
        count = 0
        start_pointer = 0
        end_pointer = 0
        while start_pointer < len(start) and end_pointer < len(end):
            if start[start_pointer] <= end[end_pointer]:
                count += 1
                start_pointer+=1
            else:
                count -= 1
                end_pointer += 1
            max_len = max(count, max_len)
        
        return max_len


        #Sliding Window
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







        