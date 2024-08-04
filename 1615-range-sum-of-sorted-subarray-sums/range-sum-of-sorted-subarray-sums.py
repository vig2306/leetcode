class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        sub_sum = []
        
        for i in range(n):
            curr_sum = 0 
            for j in range(i,n):
                curr_sum = curr_sum + nums[j]
                sub_sum.append(curr_sum)
        
        sub_sum.sort()
        ans = sum(sub_sum[left-1:right]) % mod
        return ans





        