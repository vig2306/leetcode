class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefixSum = [[0 for _ in range(n)] for _ in range(2)]
        prefixSum[0][0] = grid[0][0]
        prefixSum[1][0] = grid[1][0]

        for i in range(1, n):
            prefixSum[0][i] = prefixSum[0][i-1] + grid[0][i]
            prefixSum[1][i] = prefixSum[1][i-1] + grid[1][i]
        
        print(prefixSum)
        b_score = [0]*n
        b_score[0] = prefixSum[0][n-1] - prefixSum[0][0]
        for i in range(1, n):
            #Max possible scores when turned
            upScore = prefixSum[0][n-1] - prefixSum[0][i]
            downScore = prefixSum[1][i-1]
            b_score[i] = max(upScore, downScore)
        
        return min(b_score)




        