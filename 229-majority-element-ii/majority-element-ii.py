class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        cand1 = None
        cand2 = None

        for i in range(len(nums)):
            if count1 == 0 and nums[i] != cand2:
                cand1 = nums[i]
            if count2 == 0 and nums[i] != cand1:
                cand2 = nums[i]
            
            if nums[i] == cand1:
                count1 += 1
            
            if nums[i] == cand2:
                count2 += 1
            
            if nums[i] != cand1 and nums[i] != cand2:
                count1 -= 1
                count2 -= 1
        
        result = []
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if nums[i] == cand1:
                count1 += 1
            if nums[i] == cand2:
                count2 += 1
        
        if count1 > len(nums)//3:
            result.append(cand1)
        if count2 > len(nums)//3:
            result.append(cand2)
        
        return result


            
