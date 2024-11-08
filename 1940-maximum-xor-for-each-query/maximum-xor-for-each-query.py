class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        total_xor = 0
        for num in nums:
            total_xor = total_xor ^ num

        mask = 2**(maximumBit) - 1
        
        res = []
        for i in range(len(nums)-1,-1,-1):
            res.append(total_xor ^ mask)
            total_xor ^= nums[i]

        return res
        