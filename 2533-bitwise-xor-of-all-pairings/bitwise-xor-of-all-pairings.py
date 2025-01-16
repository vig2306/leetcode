class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        res = 0
        if m%2 != 0:   
            for i in range(n):
                res = res ^ nums1[i]
        
        if n%2 != 0:    
            for j in range(m):
                res = res ^ nums2[j]
        
        return res

        