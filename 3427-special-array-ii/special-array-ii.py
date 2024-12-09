class Solution:
    #Brute Force -> TC: O(N*Q), SC: O(1)
    #isParityTrue is used only in bruteforce

    # def isParityTrue(self, nums, start_ind, end_ind):
    #     parity = nums[start_ind]%2
    #     for i in range(start_ind+1, end_ind+1):
    #         if parity == nums[i] % 2:
    #             return False
    #         parity = nums[i]%2
        
    #     return True

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        result = []
        prefix = [0, 1]
        parity = nums[0]%2
        for i in range(1, len(nums)):
            if parity == nums[i] % 2:
                prefix.append(prefix[i])
            else:
                prefix.append(prefix[i]+1)
            
            parity = nums[i] % 2
        
        for query in queries:
            start = query[0]
            end = query[1]
            numbers_in_range = end - start + 1
            if numbers_in_range == prefix[end+1] - prefix[start+1] + 1:
                result.append(True)
            else:
                result.append(False)

            # print(prefix)
        return result


        
        
        #Brute Force
        # result = []
        # for query in queries:
        #     start = query[0]
        #     end = query[1]
        #     isParity = self.isParityTrue(nums, start, end)
        #     result.append(isParity)
        
        # return result


        