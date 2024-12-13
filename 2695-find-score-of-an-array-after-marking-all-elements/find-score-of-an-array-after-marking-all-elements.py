class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        sorted_nums = []
        for i in range(len(nums)):
            sorted_nums.append((nums[i], i))
        
        sorted_nums.sort()
        marked = [0]*len(nums)
        
        for i in range(len(sorted_nums)):
            num, index = sorted_nums[i]
            if marked[index] == 0:
                score += num
                marked[index] = 1
                if index - 1 >= 0:
                    marked[index-1] = 1
                if index + 1 < len(nums):
                    marked[index+1] = 1

        return score

        