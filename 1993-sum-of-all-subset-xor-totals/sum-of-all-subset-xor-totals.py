class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans = []
        n = len(nums)
        def xorsum(ind, res):
            if ind == n:
                ans.append(res)
                return
            
            xorsum(ind+1, res^nums[ind])
            xorsum(ind+1, res)

        xorsum(0,0)
        return sum(ans)


        