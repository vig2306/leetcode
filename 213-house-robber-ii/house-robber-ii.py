class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        two_max = 0
        one_max = 0
        ans = 0
        for index in range(len(nums)-1, 0, -1):
            take = nums[index] + two_max
            not_take = one_max
            ans = max(take, not_take)
            two_max = one_max
            one_max = ans
        first_max = one_max
        two_max = 0
        one_max = 0
        ans = 0
        for index in range(len(nums)-2, -1, -1):
            take = nums[index] + two_max
            not_take = one_max
            ans = max(take, not_take)
            two_max = one_max
            one_max = ans
        

        second_max = one_max
        return max(first_max, second_max)
        