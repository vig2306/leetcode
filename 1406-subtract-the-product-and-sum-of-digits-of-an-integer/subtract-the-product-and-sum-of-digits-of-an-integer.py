class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total_sum = 0
        product = 1
        while n > 0:
            rem = n%10
            total_sum += rem
            product *= rem
            n = n // 10
        
        return product - total_sum
        