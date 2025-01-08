class Solution:

    def recursion(self, cost, index):
        if index == 0 or index == 1:
            return cost[index]
        
        if self.memo[index] != -1:
            return self.memo[index]
        
        one_step_cost = cost[index] + self.recursion(cost, index-1)
        two_step_cost = cost[index] + self.recursion(cost, index-2)

        self.memo[index] = min(one_step_cost, two_step_cost)

        return self.memo[index]
  
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = [-1]*len(cost)
        cost1 = self.recursion(cost, len(cost)-1)
        cost2 = self.recursion(cost, len(cost)-2)
        min_cost = min(cost1, cost2)

        return min_cost
        

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
        