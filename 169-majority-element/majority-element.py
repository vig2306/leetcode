class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cand = None

        for i in range(len(nums)):
            if count == 0:
                cand = nums[i]
            
            count = count + 1 if nums[i] == cand else count-1
        
        return cand
        