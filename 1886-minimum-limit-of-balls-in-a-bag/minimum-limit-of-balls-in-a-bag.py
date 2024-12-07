class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # 1 2 3 4 5 6 7 8 

        # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
        
        left = 1
        right = max(nums)
        while left < right:
            mid = (left+right) // 2
            operations = 0
            for i in range(len(nums)):
                curr_op = nums[i] // mid
                mod = nums[i] % mid
                if curr_op > 0:
                    if mod == 0:
                        operations += curr_op - 1
                    else:
                        operations += curr_op
            
            if operations > maxOperations:
                left = mid + 1
            else:
                right = mid

        return right