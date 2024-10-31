class Solution:

    # def recur(self, nums, curr, prev_index):
    #     if curr == len(nums):
    #         return 0
    
        
    #     if self.memo[curr][prev_index+1] != -1:
    #         return self.memo[curr][prev_index+1]

    #     #Take
    #     take = 0
    #     if prev_index == -1 or nums[prev_index] < nums[curr]:
    #         take = 1 + self.recur(nums, curr+1, curr)

    #     #Not take
    #     notTake = 0 + self.recur(nums, curr+1, prev_index)

    #     self.memo[curr][prev_index+1] = max(take, notTake)
    #     return self.memo[curr][prev_index+1]

    def recursion(self, robot, factory_flattened, factory_index, robot_index):

        if robot_index == len(robot):
            self.memo[robot_index][factory_index] == 0
            return 0
        
        if factory_index == len(factory_flattened):
            self.memo[robot_index][factory_index] == float('inf')
            return float('inf')
        
        if self.memo[robot_index][factory_index] != -1:
            return self.memo[robot_index][factory_index]
        
        take = self.recursion(robot, factory_flattened, factory_index + 1, robot_index + 1) + abs(robot[robot_index] - factory_flattened[factory_index])
        notTake = self.recursion(robot, factory_flattened, factory_index + 1, robot_index)

        self.memo[robot_index][factory_index] = min(take, notTake)

        return min(take, notTake) 

    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        flat_factory = []
        self.memo = []
        for fact in factory:
            for j in range(fact[1]):
                flat_factory.append(fact[0])
        
        for i in range(len(robot)+1):
            curr = []
            for j in range(len(flat_factory)+1):
                curr.append(-1)
            self.memo.append(curr)
        
        # print(flat_factory)
        # print(self.memo)
        result = self.recursion(robot, flat_factory, 0, 0)

        # for i in range(len(factories)):
        return result
            

        