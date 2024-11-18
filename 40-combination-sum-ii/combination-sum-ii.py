class Solution:
    def recursion(self, index, target, nums, subset):
        if index == len(nums):
            if target == 0:
                self.result.append(subset.copy())
            return
        # PICK Element if less than curr target value
        if nums[index] <= target:
            subset.append(nums[index])
            self.recursion(index+1, target - nums[index], nums, subset)
            subset.pop()
        
        while index < len(nums)-1 and nums[index] == nums[index+1]:
            index += 1

        self.recursion(index+1, target, nums, subset)

        return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.result = []
        self.recursion(0, target, candidates, [])

        return self.result
        