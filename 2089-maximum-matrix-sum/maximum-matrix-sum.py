class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negativeCount = 0
        totalSum = 0
        minAbsVal = float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                minAbsVal = min(minAbsVal, abs(matrix[i][j]))
                totalSum += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    negativeCount += 1
        
        if negativeCount%2 != 0:
            totalSum -= 2*minAbsVal
        # print(totalSum)
        return totalSum
            
                



        