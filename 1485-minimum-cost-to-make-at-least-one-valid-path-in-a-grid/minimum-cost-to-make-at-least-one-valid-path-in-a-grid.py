class Solution:
    def isValid(self, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j>= n:
            return False
        return True

    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        min_cost = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        min_cost[0][0] = 0
        pq = []
        pq.append((0, 0, 0)) #(cost, i, j)
        heapq.heapify(pq)

        while pq:
            curr_cost, i, j = heapq.heappop(pq)

            for d in range(len(directions)):
                x = i + directions[d][0]
                y = j + directions[d][1]

                if self.isValid(x,y,m,n):

                    if d == grid[i][j] - 1:
                        new_cost = curr_cost
                    else:
                        new_cost = curr_cost + 1
                    
                    if new_cost < min_cost[x][y]:
                        min_cost[x][y] = new_cost
                        heapq.heappush(pq, (new_cost, x, y))

        return min_cost[m-1][n-1]
                    

            