class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_streak = 0
        for x in set_nums:
            curr_count = 0
            if x-1 not in set_nums:
                num = x
                while num in set_nums:
                    num = num + 1
                    curr_count += 1
            max_streak = max(max_streak, curr_count)
        
        return max_streak
            


        