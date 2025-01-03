class Solution:
    def climbStairs(self, n: int) -> int:
        #Why is this similar to fibonnacci types:
        #Step 3 = 3 ways
        #Step 4 = 5 ways

    
        stepCount = []
        #For n = 1 and 2
        stepCount.append(1)
        stepCount.append(2)

        for i in range(2, n):
            count = stepCount[i-1] + stepCount[i-2]
            stepCount.append(count)
        
        return stepCount[n-1]