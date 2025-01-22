class Solution:
    def isValid(self, i, j, m, n):
        if i < 0 or j < 0 or i > m-1 or j > n-1:
            return False
        
        return True

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        heights = [[-1 for _ in range(n)] for _ in range(m)]
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        # visited = [[0 for _ in range(n)] for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    queue.append((0, i, j)) #cost, i, j
        

        while queue:
            length = len(queue)
            for _ in range(length):
                cost, i, j = queue.popleft()
                for direc in directions:
                    x = i + direc[0]
                    y = j + direc[1]
                    if self.isValid(x,y,m,n) and heights[x][y] == -1:
                        heights[x][y] = cost+1
                        queue.append((cost+1,x,y))
        
        return heights

            
        

        