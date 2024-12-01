class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        set_nums = set()
        for num in arr:
            if 2*num in set_nums or (num%2==0 and num//2 in set_nums):
                return True
            
            set_nums.add(num)
        
        return False
        