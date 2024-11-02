class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        ans = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_map:
                ans = [i, diff_map[diff]]
                break
            else:
                diff_map[nums[i]] = i
        
        return ans
        

        