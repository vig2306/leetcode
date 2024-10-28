class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # print("Before", len(nums))
        # nums = list(set(nums))
        hash_set = set(nums)
        max_len = 0
        for num in nums:
            curr_len = 0
            cur_num = num

            while cur_num in hash_set:
                curr_len += 1

                # if cur_num**2 > 10**5:
                #     break
                
                cur_num *= cur_num
            
            max_len = max(max_len, curr_len)
            if max_len == 5:
                return max_len
        
        return max_len if max_len > 1 else -1


            
        