class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        con = set()
        for i in range(len(nums)):
            if nums[i] in con:
                return True
            else:
                con.add(nums[i])

        return False
        