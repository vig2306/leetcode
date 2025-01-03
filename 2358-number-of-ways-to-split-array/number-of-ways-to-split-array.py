class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        count = 0
        for i in range(1, len(nums)):
            prefixSum.append(nums[i]+prefixSum[i-1])
        n = len(prefixSum)
        print(prefixSum)
        for i in range(len(prefixSum)-1):
            print(prefixSum[i], prefixSum[n-i-1])
            if prefixSum[i] >= prefixSum[n-1] - prefixSum[i]:
                count += 1
        
        return count

        