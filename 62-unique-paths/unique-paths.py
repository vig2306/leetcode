class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []
        for i in range(m):
            curr = []
            for j in range(n):
                if j == 0 or i ==0:
                    curr.append(1)
                    continue

                curr.append(0)
            
            grid.append(curr)
        
        for i in range(1, m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        
        return grid[m-1][n-1]

        