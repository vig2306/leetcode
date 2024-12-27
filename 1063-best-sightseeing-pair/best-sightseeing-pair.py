class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score = float('-inf')
        n = len(values)
        left_values = []

        for i in range(n):
            left_values.append(values[i]+i)
        
        maxJValue = values[n-1] - (n-1)
        for j in range(n-2,-1,-1):
            maxJValue = max(maxJValue, values[j+1] - (j+1))
            score = left_values[j] + maxJValue
            max_score = max(score, max_score)
        
        return max_score

        
    # def maxScoreSightseeingPair(self, values: List[int]) -> int:
    #     #Formula: v[i] + v[j] + i-j = v[i] + i + (v[j] - j)
    #     #IValues: contains V[i] + i
    #     #JValues: contains V[j] - j
    #     #Convert IValues -> max value till index i
    #     #MaxJValues -> max value from right till index i - 1
    #     #Score[i] = IValues[i] + MaxJValues[i]
    #     #TC -> O(N) -> Multiple Pass
    #     #SC -> O(N) -> Multiple Arrays

    #     max_score = float('-inf')


    #     IValues = []
    #     JValues = []

    #     for i in range(len(values)):
    #         IValues.append(values[i]+i)
    #         JValues.append(values[i]-i)
        
    #     for i in range(1, len(IValues)):
    #         IValues[i] = max(IValues[i], IValues[i-1])
        
    #     # print(IValues)
    #     maxJValues = [float('-inf')]*len(values)
    #     for i in range(len(values)-2,-1,-1):
    #         maxJValues[i] = max(JValues[i+1], maxJValues[i+1])
        
    #     print(maxJValues)

    #     for i in range(len(values)-1):
    #         max_score = max(max_score, IValues[i]+maxJValues[i])
        
    #     return max_score

        # for i in range(len(values)):
        #     for j in range(i+1, len(values)):
        #         score = values[i] + values[j] + i - j
        #         max_score = max(score, max_score)
        
        # return max_score

