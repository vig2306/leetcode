class Solution:

    def recursion(self, triangle, i, j, m):
        if i == m - 1:
            return triangle[m-1][j]
        
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        
        down = triangle[i][j] + self.recursion(triangle, i+1, j, m)
        diagonal = triangle[i][j] + self.recursion(triangle, i+1, j+1, m)

        self.memo[i][j] = min(down, diagonal)

        return self.memo[i][j]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        self.memo = [[-1 for _ in range(m)] for _ in range(m)]
        result = self.recursion(triangle, 0, 0, m)

        return result

    ##Recursion  
    # def recursion(self, triangle, i, j, m):
    #     if i == m - 1:
    #         return triangle[m-1][j]
        
    #     down = triangle[i][j] + self.recursion(triangle, i+1, j, m)
    #     diagonal = triangle[i][j] + self.recursion(triangle, i+1, j+1, m)

    #     return min(down, diagonal)

    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     m = len(triangle)
    #     result = self.recursion(triangle, 0, 0, m)

    #     return result
        