class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        #Optimal:

        totalSum = sum(nums)
        count = 0
        curr_sum = 0
        for i in range(len(nums)-1):
            curr_sum += nums[i]
            if curr_sum >= totalSum - curr_sum:
                count+=1
        
        return count


        #Sub-Optimal: -> Prefix Sum
        #TC -> O(N)
        # #SC -> O(N)
        # prefixSum = [nums[0]]
        # count = 0
        # for i in range(1, len(nums)):
        #     prefixSum.append(nums[i]+prefixSum[i-1])
        # n = len(prefixSum)
        # print(prefixSum)
        # for i in range(len(prefixSum)-1):
        #     print(prefixSum[i], prefixSum[n-i-1])
        #     if prefixSum[i] >= prefixSum[n-1] - prefixSum[i]:
        #         count += 1
        
        # return count

        