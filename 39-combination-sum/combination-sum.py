class Solution:
    def recursion(self, nums, index, subset, target, curr_sum):
        if curr_sum > target or index >= len(nums):
            return

        if curr_sum == target:
            self.result.append(subset.copy())
            return

        subset.append(nums[index])
        self.recursion(nums, index, subset, target, curr_sum+nums[index])
        subset.pop()
        self.recursion(nums, index+1, subset, target, curr_sum)

        return
        

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.recursion(candidates, 0, [], target, 0)

        return self.result


        