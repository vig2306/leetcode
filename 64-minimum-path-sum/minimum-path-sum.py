class Solution:
    #Memo
    def recursion(self, grid, i, j):
        if i < 0 or j < 0:
            return float('inf')
        if i==0 and j==0:
            return grid[0][0]
        
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        
        up = grid[i][j] + self.recursion(grid, i-1, j)
        left = grid[i][j] + self.recursion(grid, i, j-1)

        self.memo[i][j] = min(up,left)

        return self.memo[i][j]
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.memo = [[-1 for _ in range(n)] for _ in range(m)]
        res = self.recursion(grid, m-1, n-1)
        return res
    
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
        