class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bitmap = []
        for i in range(len(nums)):
            bitmap.append(bin(nums[i]).count("1"))
        
        values = nums.copy()

        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if values[j] <= values[j+1]:
                    continue
                if bitmap[j] == bitmap[j+1]:
                    values[j], values[j+1] = values[j+1], values[j]
                else:
                    return False
            
        return True



        