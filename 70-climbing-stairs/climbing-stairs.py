class Solution:
    def climbStairs(self, n: int) -> int:
        #Why is this similar to fibonnacci types:
        #Step 3 = 3 ways
        #Step 4 = 5 ways
        #F(N) = F(N-1) + F(N-2)

        #Optimal -> Space Optimized:

        #TC -> O(N)
        #SC -> O(1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        first = 1
        second = 2
        count = 0

        for i in range(2, n):
            count = first + second
            first = second
            second = count
        
        return count

        #Optimal -> With Space:
        #TC -> O(N)
        #SC -> O(N)

        # stepCount = []
        # #For n = 1 and 2
        # stepCount.append(1)
        # stepCount.append(2)

        # for i in range(2, n):
        #     count = stepCount[i-1] + stepCount[i-2]
        #     stepCount.append(count)
        
        # return stepCount[n-1]