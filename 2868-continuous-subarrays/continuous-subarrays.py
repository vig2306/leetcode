# [1,42,41,42,20,41,40,39,38]

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:        
        i, j, count = 0, 0, 0
        while i < len(nums):
            curr_max, max_idx = nums[i], i
            curr_min, min_idx = nums[i], i
            # j = i + 1

            while j < len(nums) and abs(nums[j] - curr_max) <= 2 and abs(nums[j] - curr_min) <= 2:
                if nums[j] >= curr_max:
                    curr_max, max_idx= nums[j], j
                if nums[j] <= curr_min:
                    curr_min, min_idx = nums[j], j
                j += 1

            count += ((j - i) * (j - i + 1)) // 2

            if j == len(nums):
                break
            elif abs(nums[j] - curr_max) > 2:
                i = max_idx + 1
            else:
                i = min_idx + 1

            max_i_giving_valid_window_with_j = i
            for k in range(i, j + 1):
                if abs(nums[j] - nums[k]) > 2:
                    max_i_giving_valid_window_with_j = k

            repeated_size = j - 1 - max_i_giving_valid_window_with_j + 1
            count -= (repeated_size * (repeated_size + 1)) // 2
            i = max_i_giving_valid_window_with_j

        return count


# Sub-optimal
# class Solution:
#     def continuousSubarrays(self, nums: List[int]) -> int:
#         count = 0

#         for i in range(len(nums)):
#             curr_count = 1
#             curr_max = nums[i]
#             curr_min = nums[i]

#             for j in range(i+1, len(nums)):
#                 if abs(nums[j] - curr_max) <= 2 and abs(nums[j] - curr_min) <= 2:
#                     curr_max = max(curr_max, nums[j])
#                     curr_min = min(curr_min, nums[j])
#                     curr_count += 1
#                 else:
#                     break

#             count += curr_count
#                 4 4 4  2 1
#         return count

