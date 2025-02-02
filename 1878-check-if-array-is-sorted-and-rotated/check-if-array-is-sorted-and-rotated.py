class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        startIndex = -1
        # array = []
        for i in range(0, n):
            # array.append(nums[i])
            prev = nums[i-1]
            nextnumber = nums[(i+1)%n]
            
            if nums[i] < prev  and nums[i] <= nextnumber:
                startIndex = i
        
        print(startIndex)
        if startIndex == -1:
            return True
        
        # for i in range(n):
        #     array.append(nums[i])
        
        # print(array)
        
        for i in range(n-1):
            curr_index = (i + startIndex)%n
            next_index = (i + startIndex + 1)%n
            if nums[curr_index] > nums[next_index]:
                return False

        return True