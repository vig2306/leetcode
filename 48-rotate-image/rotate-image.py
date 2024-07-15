class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        position = len(matrix)
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[i])):
                matrix[i][j] , matrix[j][i] =  matrix[j][i] , matrix[i][j]
        n = len(matrix)

        for i in range(len(matrix)):
            if n%2 == 0:
                for j in range(0, (n//2)):
                    matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
                
            else:
                for j in range(0, (n//2) + 1):
                    matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

 





            

        