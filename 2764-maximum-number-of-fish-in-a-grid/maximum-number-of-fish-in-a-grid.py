class Solution:
    def isValid(self, i, j, m, n):
        if i < 0 or j < 0 or i > m-1 or j > n-1:
            return False
        
        return True
    
    def bfs(self, grid, a, b, m, n):
        queue = deque()
        queue.append((a, b))
        maxFish = grid[a][b]
        self.visited[a][b] = 1
        while queue:
            i, j = queue.popleft()
            
            for d in self.directions:
                x = i + d[0]
                y = j + d[1]
                if self.isValid(x, y, m, n) and self.visited[x][y] == 0 and grid[x][y] > 0:
                    self.visited[x][y] = 1
                    queue.append((x, y))
                    maxFish += grid[x][y]
        
        return maxFish

    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxFish = 0
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]
        self.visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and self.visited[i][j] == 0:
                    maxFish = max(maxFish, self.bfs(grid, i, j, m, n))
        
        return maxFish



        