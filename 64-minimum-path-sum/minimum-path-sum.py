class Solution:
    #Space optimised
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prev = [0 for _ in range(n)]
        for i in range(m):
            curr = [0 for _ in range(n)]
            for j in range(n):
                if i == 0 and j == 0:
                    curr[j] = grid[i][j]
                    continue
                up = float('inf')
                left = float('inf')
                if i > 0:
                    up = grid[i][j] + prev[j]
                if j > 0:
                    left = grid[i][j] + curr[j-1]
                
                curr[j] = min(up, left)
            
            prev = curr

        return prev[n-1]

    # #Tabulation
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     dp = [[-1 for _ in range(n)] for _ in range(m)]
    #     for i in range(m):
    #         for j in range(n):
    #             if i == 0 and j == 0:
    #                 dp[i][j] = grid[i][j]
    #                 continue
    #             up = float('inf')
    #             left = float('inf')
    #             if i > 0:
    #                 up = grid[i][j] + dp[i-1][j]
    #             if j > 0:
    #                 left = grid[i][j] + dp[i][j-1]
                
    #             dp[i][j] = min(up, left)

    #     return dp[m-1][n-1]

    #Memo
    # def recursion(self, grid, i, j):
    #     if i < 0 or j < 0:
    #         return float('inf')
    #     if i==0 and j==0:
    #         return grid[0][0]
        
    #     if self.memo[i][j] != -1:
    #         return self.memo[i][j]
        
    #     up = grid[i][j] + self.recursion(grid, i-1, j)
    #     left = grid[i][j] + self.recursion(grid, i, j-1)

    #     self.memo[i][j] = min(up,left)

    #     return self.memo[i][j]
        
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     self.memo = [[-1 for _ in range(n)] for _ in range(m)]
    #     res = self.recursion(grid, m-1, n-1)
    #     return res
    
    # #Recursion
    # def recursion(self, grid, i, j):
    #     if i < 0 or j < 0:
    #         return float('inf')
    #     if i==0 and j==0:
    #         return grid[0][0]
        
    #     up = grid[i][j] + self.recursion(grid, i-1, j)
    #     left = grid[i][j] + self.recursion(grid, i, j-1)

    #     return min(up, left)
        
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     res = self.recursion(grid, m-1, n-1)
    #     return res
        