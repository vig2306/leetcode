class TicTacToe:


    0,0
    1,1
    2,2

    [0, 1]
    [1, 2]
    rowA = [1, 0]
    rowB = [0, 1]
    colA = [0, 1]
    colB = [0, 1]
    diag1A = 0
    diag2A = 0
    diag1B = 0
    diag2B = 0

    def __init__(self, n: int):
        self.n = n
        self.rowA = [0]*(n)
        self.rowB = [0]*(n)
        self.colA = [0]*(n)
        self.colB = [0]*(n)
        self.diag1A = 0
        self.diag2A = 0
        self.diag1B = 0
        self.diag2B = 0

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.rowA[row] += 1
            self.colA[col] += 1
            if row == col:
                self.diag1A += 1
            
            if row + col == self.n - 1:
                self.diag2A += 1

            if (self.rowA[row] == self.n or 
                self.colA[col] == self.n or
                self.diag1A == self.n or
                self.diag2A == self.n):
                return 1

        if player == 2:
            self.rowB[row] += 1
            self.colB[col] += 1
            if row == col:
                self.diag1B += 1
            
            if row + col == self.n - 1:
                self.diag2B += 1

            if (self.rowB[row] == self.n or 
                self.colB[col] == self.n or
                self.diag1B == self.n or
                self.diag2B == self.n):
                return 2
        
        return 0
        

        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)