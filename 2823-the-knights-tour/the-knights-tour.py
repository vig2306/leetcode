class Solution:
    def is_invalid(self,r,c,m,n):
        if r<0 or r>m-1 or c<0 or c > n - 1:
            return True
        return False

    def dfs(self,r,c,m,n,count):
        self.visited[r][c] = count

        if count == m * n:
            if not self.set_final:
                self.set_final = True
                for i in range(len(self.final)):
                    for j in range(len(self.final[0])):
                        self.final[i][j] = self.visited[i][j] - 1
            return

        for di, dj in self.moves:
            ni, nj = r + di, c + dj

            if not self.is_invalid(ni, nj, m, n) and self.visited[ni][nj] == 0 and not self.set_final:
                self.dfs(ni, nj, m, n, count + 1)
                self.visited[ni][nj] = 0


    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        self.visited = [[0 for i in range(n)] for j in range(m)]
        self.final = [[0 for i in range(n)] for j in range(m)]
        self.set_final = False
        self.visited[r][c] = 1
        self.moves = [[1,2], [-1,2], [1,-2], [-1,-2], [2,1], [-2,1], [2,-1], [-2,-1]]
        self.dfs(r,c,m,n,1)

        return self.final
        