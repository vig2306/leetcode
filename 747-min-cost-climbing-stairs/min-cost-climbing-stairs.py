class Solution:
    #Space Optimised DP
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        two_prev_step = cost[0]
        one_prev_step = cost[1]
        for i in range(2, n):

            curr_cost = min(cost[i]+one_prev_step, cost[i]+two_prev_step)

            two_prev_step = one_prev_step
            one_prev_step = curr_cost

        return min(two_prev_step, one_prev_step)


    #Tabulation
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     dp = [-1]*len(cost)
    #     n = len(dp)
    #     dp[0] = cost[0]
    #     dp[1] = cost[1]
    #     for i in range(2, len(dp)):

    #         one_step_cost = cost[i] + dp[i-1]
    #         two_step_cost = cost[i] + dp[i-2]

    #         dp[i] = min(one_step_cost, two_step_cost)

    #     return min(dp[n-1], dp[n-2])


    #Recursion with Memo 

    # def recursion(self, cost, index):
    #     if index == 0 or index == 1:
    #         self.memo[index] = cost[index]
    #         return cost[index]
        
    #     if self.memo[index] != -1:
    #         return self.memo[index]
        
    #     one_step_cost = cost[index] + self.recursion(cost, index-1)
    #     two_step_cost = cost[index] + self.recursion(cost, index-2)

    #     self.memo[index] = min(one_step_cost, two_step_cost)

    #     return self.memo[index]
  
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     self.memo = [-1]*len(cost)
    #     cost1 = self.recursion(cost, len(cost)-1)
    #     cost2 = self.recursion(cost, len(cost)-2)
    #     min_cost = min(cost1, cost2)

    #     return min_cost
        

    #Recursion
    # def recursion(self, cost, index):
    #     if index == 0 or index == 1:
    #         return cost[index]
        
    #     one_step_cost = cost[index] + self.recursion(cost, index-1)
    #     two_step_cost = cost[index] + self.recursion(cost, index-2)

    #     return min(one_step_cost, two_step_cost)

        
        
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     cost1 = self.recursion(cost, len(cost)-1)
    #     cost2 = self.recursion(cost, len(cost)-2)
    #     min_cost = min(cost1, cost2)

    #     return min_cost
        