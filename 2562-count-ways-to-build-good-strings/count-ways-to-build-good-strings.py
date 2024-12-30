class Solution:
    def recursion(self, zero_count, one_count, length):
        if length == 0:
            return 1
        
        if length < 0:
            return 0
        
        if self.memo[length] != -1:
            return self.memo[length]

        take0 = 0
        take1 = 0
        if zero_count <= length:
            take0 = self.recursion(zero_count, one_count, length-zero_count)
        
        if one_count <= length:
            take1 = self.recursion(zero_count, one_count, length-one_count)

        self.memo[length] = (take0 + take1)
        
        return (take0 + take1)




    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        self.mod = 10**9 + 7
        self.memo = [-1]*(high+1)
        count = 0
        for length in range(low, high+1):
            count += self.recursion(zero, one, length)
            count = count % self.mod

        return count % self.mod
