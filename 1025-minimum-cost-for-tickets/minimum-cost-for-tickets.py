class Solution:

    def recursion(self, days, costs, i):
        if i == len(days):
            return 0
        
        if self.memo[i] != float('inf'):
            return self.memo[i]
      
        next_index = i
        res = float('inf')

        for k in range(len(costs)):
            if k == 0:
                duration = 1
            if k == 1:
                duration = 7
            if k ==2:
                duration = 30
            while next_index < len(days) and days[next_index] < days[i]+duration:
                next_index+=1
            res = min(res, costs[k] + self.recursion(days, costs, next_index))
        
        self.memo[i] = res

        return self.memo[i]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        self.memo = [float('inf')]*len(days)
        min_cost = self.recursion(days, costs, 0)
        return min_cost

        