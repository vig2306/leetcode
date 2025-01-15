class Solution:
    def isValid(self, i, j, m, n):
        if i < 0 or j < 0 or i > m-1 or j > n-1:
            return False
        return True

    def bfs(self, grid, p, q, m, n):
        queue = [(p,q)]
        self.visited[p][q] = 1
        area = 1
        while queue:
            i, j = queue.pop(0)
            for node in self.directions:
                x = i + node[0]
                y = j + node[1]
                if self.isValid(x, y, m, n) and grid[x][y] == 1 and self.visited[x][y] == 0:
                    queue.append((x,y))
                    self.visited[x][y] = 1
                    area += 1
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        self.directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.visited = [[0 for i in range(n)] for j in range(m)]
        max_area = 0
        for i in range(m):
            for j in range(n):
                if self.visited[i][j] == 0 and grid[i][j] == 1:
                    area = self.bfs(grid, i,j,m,n)
                    max_area = max(area, max_area)
        
        return max_area

        