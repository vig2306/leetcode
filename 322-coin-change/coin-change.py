class Solution:
    def recursion(self, coins, amount):
        if amount == 0:
            self.memo[amount] = 0
            return 0
        elif amount < 0:
            return float('inf')
        
        if self.memo[amount] != -1:
            return self.memo[amount]

        # PICK Element if less than curr target value
        ans = float('inf')
        take = float('inf')
        for coin in coins:
            if amount - coin >= 0:
                take = 1 + self.recursion(coins, amount - coin)

            ans = min(take, ans)
        self.memo[amount] = ans
        return ans
            
            
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = [-1] * (amount+1) 
        ans = self.recursion(coins, amount)
        return -1 if ans == float('inf') else ans

        