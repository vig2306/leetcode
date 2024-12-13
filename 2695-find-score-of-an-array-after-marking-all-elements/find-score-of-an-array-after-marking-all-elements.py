class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        sorted_nums = []
        for i in range(len(nums)):
            sorted_nums.append((nums[i], i))
        
        sorted_nums.sort()
        marked_index = set()
        
        for i in range(len(sorted_nums)):
            num, index = sorted_nums[i]
            if index not in marked_index:
                score += num
                marked_index.add(index)
                marked_index.add(index-1)
                marked_index.add(index+1)
            


        return score

        