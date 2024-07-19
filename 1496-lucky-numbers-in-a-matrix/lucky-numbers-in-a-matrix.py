class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        max_rowMin = 0
        min_colMax = 10**5 + 1

        for i in range(m):
            rowMin = min(matrix[i])
            max_rowMin = max(rowMin, max_rowMin)
        
        for i in range(n):
            colMax = 0 
            for j in range(m):
                print(j,i)
                colMax = max(colMax, matrix[j][i])
            min_colMax = min(colMax, min_colMax)
        
        return [max_rowMin] if min_colMax == max_rowMin else []

        