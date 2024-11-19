class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = 0
        r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r+1):
                curr_jump = i + nums[i]
                farthest = max(curr_jump, farthest)
            
            l = r+1
            r = farthest
            jumps = jumps+1
        
        return jumps
        

        