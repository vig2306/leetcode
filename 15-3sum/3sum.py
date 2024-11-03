'''
 a + b = - c
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Two pointer with sorting (First optimal Approach)
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = len(nums) - 1
            j = i + 1
            while j<k:
                trip_sum = nums[i] + nums[j] + nums[k]
                if trip_sum < 0:
                    j = j + 1
                elif trip_sum > 0:
                    k = k - 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1
        return res
                    

        #Hashing Approach but gives TLE for all zeroes
        # res = set()
        # for i in range(len(nums)):
        #     target_set = set()
        #     for j in range(i+1, len(nums)):
        #         target = -(nums[i] + nums[j])
        #         if target in target_set:
        #             temp = sorted([nums[i], nums[j], target])
        #             res.add(tuple(temp))
        #         target_set.add(nums[j])
        # result = [list(x) for x in res]
        # return result


        