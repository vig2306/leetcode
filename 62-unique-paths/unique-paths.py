class Solution:

    #Memo
    def recursion(self, i, j):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        
        up = self.recursion(i-1, j)
        left = self.recursion(i, j-1)

        self.memo[i][j] = up + left
        
        return self.memo[i][j]

    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = [[-1 for _ in range(n)] for _ in range(m)]
        print(self.memo)
        result = self.recursion(m-1, n-1)
        return result



    #Recursion
    # def recursion(self, i, j):
    #     if i == 0 and j == 0:
    #         return 1
    #     if i < 0 or j < 0:
    #         return 0
        
    #     up = self.recursion(i-1, j)
    #     left = self.recursion(i, j-1)
        
    #     return up + left
    # def uniquePaths(self, m: int, n: int) -> int:
    #     result = self.recursion(m-1, n-1)
    #     return result
        