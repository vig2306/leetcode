class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        rowServers = [0]*(rows)
        colServers = [0]*(cols)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    rowServers[i] += 1
                    colServers[j] += 1
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if rowServers[i] == 1 and colServers[j] == 1:
                        continue

                    count += 1
        
        return count

        