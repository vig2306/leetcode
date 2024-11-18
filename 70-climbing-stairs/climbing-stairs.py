class Solution:
    def climbStairs(self, n: int) -> int:
        stepCount = []
        #for 0 steps:
        stepCount.append(1)
        stepCount.append(2)

        for i in range(2, n):
            count = stepCount[i-1] + stepCount[i-2]
            stepCount.append(count)
        
        return stepCount[n-1]
        