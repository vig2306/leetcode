class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        #add bits to the b array if 1 is present
        def add_bits(num,b):
            i = 0
            while num >0:
                b[i] += num & 1
                num >>= 1
                i+=1
         #remove bits from b array if 1 is present
        def remove_bits(num,b):
            i = 0
            while num > 0:
                b[i] -= num & 1
                num >>= 1
                i+=1
        #convert bit to number
        def constructed_val(b):
            res = 0
            for i in range(32):
                if b[i]:
                    res |= (1<<i)
            return res

        left = 0

        b = [0]*32
        ans = 10000000
        for right in range(len(nums)):
            add_bits(nums[right],b)

            while constructed_val(b) >= k and left <= right:
                ans = min(ans,right-left+1)
                if ans == 1:
                    return 1
                remove_bits(nums[left],b)
                left+=1
        
        if ans == 10000000:
            return -1
        else:
            return ans