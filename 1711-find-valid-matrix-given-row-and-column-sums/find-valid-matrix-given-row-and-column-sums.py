class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = []
        min_val = 10**8 + 1
        for i in range(len(rowSum)):
            matrix.append([])
            for j in range(len(colSum)):
                min_val = min(colSum[j], rowSum[i])
                matrix[i].append(min_val)
                colSum[j] -= min_val
                rowSum[i] -= min_val

        return matrix

        