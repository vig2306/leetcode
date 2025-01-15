class Solution:
    #Tabulation:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(0, m):
            for j in range(0, n):
                if i==0 and j==0:
                    dp[i][j] = 1
                    continue
                up = 0
                left = 0
                if i > 0 and obstacleGrid[i-1][j] == 0:
                    up = dp[i-1][j]
                if j > 0 and obstacleGrid[i][j-1] == 0:
                    left = dp[i][j-1]
                
                dp[i][j] = up + left

        return dp[m-1][n-1]

    #Memoisation:
    # def recursion(self, i, j, grid):
    #     if i==0 and j==0:
    #         return 1
    #     if i < 0 or j< 0:
    #         return 0
        
    #     if self.memo[i][j] != -1:
    #         return self.memo[i][j]
        
    #     up = 0
    #     left = 0
    #     if grid[i-1][j] == 0:
    #         up = self.recursion(i-1, j, grid)

    #     if grid[i][j-1] == 0:
    #         left = self.recursion(i, j-1, grid)
        
    #     self.memo[i][j] = up + left
        
    #     return self.memo[i][j]
        
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     m = len(obstacleGrid)
    #     n = len(obstacleGrid[0])
    #     if obstacleGrid[m-1][n-1] == 1:
    #         return 0
    #     self.memo = [[-1 for _ in range(n)] for _ in range(m)]
    #     res = self.recursion(m-1, n-1, obstacleGrid)

    #     return res

    #Recursion
    # def recursion(self, i, j, grid):
    #     if i==0 and j==0:
    #         return 1
    #     if i < 0 or j< 0:
    #         return 0
        
    #     up = 0
    #     left = 0
    #     if grid[i-1][j] == 0:
    #         up = self.recursion(i-1, j, grid)

    #     if grid[i][j-1] == 0:
    #         left = self.recursion(i, j-1, grid)
        
    #     return up + left
        
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     m = len(obstacleGrid)
    #     n = len(obstacleGrid[0])
    #     res = self.recursion(m-1, n-1, obstacleGrid)

    #     return res
        