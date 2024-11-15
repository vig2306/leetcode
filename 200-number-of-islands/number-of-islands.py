class Solution:
    def isValid(self, i, j, m, n):
        if i < 0 or j < 0 or i > m-1 or j > n-1:
            return False
        return True

    def bfs(self, grid, p, q, m, n):
        queue = [(p,q)]
        self.visited[p][q] = 1
        while queue:
            i, j = queue.pop(0)
            for node in self.directions:
                x = i + node[0]
                y = j + node[1]
                if self.isValid(x, y, m, n) and grid[x][y] == '1' and self.visited[x][y] == 0:
                    queue.append((x,y))
                    self.visited[x][y] = 1
        
        return 

    def numIslands(self, grid: List[List[str]]) -> int:
        self.directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.visited = []
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(0)
            self.visited.append(temp)
        for i in range(m):
            for j in range(n):
                if self.visited[i][j] == 0 and grid[i][j] == '1':
                    self.bfs(grid, i, j, m, n)
                    count += 1
        
        return count



        