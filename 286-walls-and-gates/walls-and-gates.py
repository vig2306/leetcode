class Solution:
    def isValid(self, i, j, rooms):
        m = len(rooms)
        n = len(rooms[0])
        if i < 0 or j < 0 or i >= m or j >= n or rooms[i][j] == -1:
            return False
        return True

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        #Intuition: DFS works but we have to call DFS for every node and each node dfs call will be m*n
        #So total DFS would be O((m*n)^2)
        #BFS from each node wont work because BFS will take the nearest position and mark them visited
        #We will not be able to reach to the node again
        #Solution is to have a multi source BFS
        #Whichever is a gate we will add to the queue and update the distance accordingly


        inf = 2^31 - 1
        queue = deque()
        m = len(rooms)
        n = len(rooms[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))
                    visited[i][j] = 1

        curr_distance = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            length = len(queue)
            for x in range(length):
                i, j = queue.popleft()
                rooms[i][j] = curr_distance
                for direc in directions:
                    x = i + direc[0]
                    y = j + direc[1]
                    if self.isValid(x, y, rooms) and visited[x][y] == 0:
                        queue.append((x,y))
                        visited[x][y] = 1
            
            curr_distance += 1
        
        return

        