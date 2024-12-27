class Solution:
    # def recursion(self, i, values):
    #     if i == len(values)-1:
    #         return float('-inf')

    #     max_score = float('-inf')
    #     for j in range(i+1, len(values)):
    #         score = values[i] + values[j] + i - j
    #         max_score = max(score, max_score)
    #         self.recursion(i+1, values)

    #     return max_score

    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        # max_score = self.recursion(0, values)
        # return max_score
        max_score = float('-inf')

        #Formula: v[i] + v[j] + i-j = v[i] + i + (v[j] - j)

        IValues = []
        JValues = []

        for i in range(len(values)):
            IValues.append(values[i]+i)
            JValues.append(values[i]-i)
        
        for i in range(1, len(IValues)):
            IValues[i] = max(IValues[i], IValues[i-1])
        
        # print(IValues)
        maxJValues = [float('-inf')]*len(values)
        for i in range(len(values)-2,-1,-1):
            maxJValues[i] = max(JValues[i+1], maxJValues[i+1])
        
        print(maxJValues)

        for i in range(len(values)-1):
            max_score = max(max_score, IValues[i]+maxJValues[i])
        
        return max_score
            

        # n = len(JValues)
        # JValues[n-2] = JValues[n-1]
        # for j in range(n-2, -1, -1):
        #     JValues[j] = max(JValues[])

        # for i in range(len(values)):
        #     for j in range(i+1, len(values)):
        #         score = values[i] + values[j] + i - j
        #         max_score = max(score, max_score)
        
        # return max_score

