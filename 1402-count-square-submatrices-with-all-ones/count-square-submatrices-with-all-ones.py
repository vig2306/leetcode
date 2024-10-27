class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = []
        for _ in range(rows):
            curr = []
            for j in range(cols):
                curr.append(0)
            
            dp.append(curr)
        
        res = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]:
                    if i == 0 or j == 0:
                        dp[i][j] = matrix[i][j]
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    res += dp[i][j]
        
        return res


        