class Solution:
    def recursion(self, nums, hashset, array):
        if len(array) == len(nums):
            self.result.append(array.copy())
            return
        
        for num in nums:
            if num not in hashset:
                hashset.add(num)
                array.append(num)
                self.recursion(nums, hashset, array)
                array.pop()
                hashset.remove(num)
        
        return
  
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.recursion(nums, set(), [])

        return self.result

        