class Solution:
    def recursion(self, nums, res, index):
        if index == -1:
            self.results.append(res.copy())
            return 
        
        res.append(nums[index])
        self.recursion(nums, res, index-1)
        res.pop()
        self.recursion(nums, res, index-1)

        return



    def subsets(self, nums: List[int]) -> List[List[int]]:

        self.results = []
        self.recursion(nums, [], len(nums)-1)

        return self.results
        
        