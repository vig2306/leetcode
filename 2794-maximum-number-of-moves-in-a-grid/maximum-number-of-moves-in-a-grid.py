class Solution:

    '''Tabulation'''
    def recursion(self, grid, r, c, m, n):
        if c == n - 1:
            self.dp[r][c] = 0
            return 0
        
        if self.dp[r][c] != -1:
            return self.dp[r][c]
        
        
        up = 0
        if r-1 < m and c+1 < n and r-1>=0 and c+1>=0 and grid[r-1][c+1] > grid[r][c]:
            up = self.recursion(grid, r-1, c+1, m, n) + 1

        side = 0
        if r < m and c+1 < n and r>=0 and c+1>=0 and grid[r][c+1] > grid[r][c]:
            side = self.recursion(grid, r, c+1, m, n) + 1

        down = 0
        if r+1 < m and c+1 < n and r+1>=0 and c+1>=0 and grid[r+1][c+1] > grid[r][c]:
            down = self.recursion(grid, r+1, c+1, m, n) + 1
        
        self.dp[r][c] = max(up, side, down)
        return max(up, side, down)
        
    
    def maxMoves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(n)] for j in range(m)]
        # print(zeros)
        for i in range(m):
            dp[i][-1] = 0
        
        for c in range(n-2, -1, -1):
            for r in range(m):

                up = 0
                if r-1 < m and c+1 < n and r-1>=0 and c+1>=0 and grid[r-1][c+1] > grid[r][c]:
                    up = dp[r-1][c+1] + 1

                side = 0
                if r < m and c+1 < n and r>=0 and c+1>=0 and grid[r][c+1] > grid[r][c]:
                    side = dp[r][c+1] + 1

                down = 0
                if r+1 < m and c+1 < n and r+1>=0 and c+1>=0 and grid[r+1][c+1] > grid[r][c]:
                    down = dp[r+1][c+1] + 1
                
                dp[r][c] = max(up, side, down)

        max_result = 0
        for i in range(m):
            result = dp[i][0]
            max_result = max(result, max_result)

        return max_result 
        

    '''Memo'''
    # def recursion(self, grid, r, c, m, n):
    #     if c == n - 1:
    #         self.dp[r][c] = 0
    #         return 0
        
    #     if self.dp[r][c] != -1:
    #         return self.dp[r][c]
        
        
    #     up = 0
    #     if r-1 < m and c+1 < n and r-1>=0 and c+1>=0 and grid[r-1][c+1] > grid[r][c]:
    #         up = self.recursion(grid, r-1, c+1, m, n) + 1

    #     side = 0
    #     if r < m and c+1 < n and r>=0 and c+1>=0 and grid[r][c+1] > grid[r][c]:
    #         side = self.recursion(grid, r, c+1, m, n) + 1

    #     down = 0
    #     if r+1 < m and c+1 < n and r+1>=0 and c+1>=0 and grid[r+1][c+1] > grid[r][c]:
    #         down = self.recursion(grid, r+1, c+1, m, n) + 1
        
    #     self.dp[r][c] = max(up, side, down)
    #     return max(up, side, down)
        
    
    # def maxMoves(self, grid: List[List[int]]) -> int:
    #     m = len(grid)
    #     n = len(grid[0])
    #     self.dp = [[-1 for i in range(n)] for j in range(m)]
    #     # print(zeros)

    #     max_result = 0
    #     for i in range(m):
    #         result = self.recursion(grid, i, 0, m, n)
    #         max_result = max(result, max_result)

    #     return max_result 
        