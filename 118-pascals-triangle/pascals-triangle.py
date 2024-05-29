class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(0, numRows):
            ans = []
            for j in range(0,i+1):
                if j == 0:
                    ans.append(1)
                elif j==i:
                    ans.append(1)
                else:
                    ans.append(res[i-1][j] + res[i-1][j-1])
            res.append(ans)
        
        return res
        