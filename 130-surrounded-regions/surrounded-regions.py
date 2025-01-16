class Solution:
    def isValid(self, x, y, board):
        m = len(board)
        n = len(board[0])
        if x < 0 or y < 0 or x >= m or y >= n:
            return False
        
        return True

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        queue = deque()
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            if board[0][j] == 'O':
                queue.append((0,j))
                visited[0][j] = 2
            
            if board[m-1][j] == 'O':
                queue.append((m-1,j))
                visited[m-1][j] = 2
        
        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i,0))
                visited[i][0] = 2
            
            if board[i][n-1] == 'O':
                queue.append((i, n-1))
                visited[i][n-1] = 2
        print(visited)
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while queue:
            length = len(queue)
            for _ in range(length):
                i, j = queue.popleft()
                for ni, nj in directions:
                    x = i + ni
                    y = j + nj
                    if self.isValid(x, y, board) and visited[x][y] == 0 and board[x][y] == 'O':
                        queue.append((x,y))
                        visited[x][y] = 2
        
        print(visited)
        
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0:
                    board[i][j] = 'X'
            
        return
        