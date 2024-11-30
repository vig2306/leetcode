class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        #Intuition: Find the shortes Path -> Djikstra
        #Only in 1 case you cant reach is if you cant move ahead from the first cell
        #if you cant go to the next cell go back and forth from the previous cell (Handled by wait time)
        '''If you can check the max(next_time+waitTime, curr_time+1)
        The above check if the curr_time is greater than the next cell time because 
        We can visit the next cell immediately then we do curr_time+1'''
        min_heap = [(0,0,0)] #Time, Row, Col 
        visited = set()
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1

        while min_heap:
            time, r, c = heapq.heappop(min_heap)
            if r == rows-1 and c == cols-1:
                return time
            
            for nx, ny in directions:
                # print(nx, ny)
                if r+nx < 0 or c+ny < 0 or r + nx == rows or c+ny == cols:
                    continue
                
                if (r+nx, c+ny) in visited:
                    continue
                
                wait_time = 0
                if abs(grid[r+nx][c+ny] - time)%2 == 0: #Condition for wait time -> see Editorial
                    wait_time = 1
                
                new_time = max(grid[r+nx][c+ny] + wait_time, time+1)
                heapq.heappush(min_heap, (new_time, r+nx, c+ny))
                visited.add((r+nx, c+ny))



        