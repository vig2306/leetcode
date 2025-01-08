class Solution:
    def recursion(self, board, word, i, j, word_index):
        if word_index == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        if board[i][j] != word[word_index]:
            return False
        if self.visited[i][j] == 1:
            return False
        
        self.visited[i][j] = 1
        res = (self.recursion(board, word, i+1, j, word_index+1) 
        or self.recursion(board, word, i-1, j, word_index+1) or 
        self.recursion(board, word, i, j-1, word_index+1) or 
        self.recursion(board, word, i, j+1, word_index+1))
            
        self.visited[i][j] = 0
        
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                result = self.recursion(board, word, i, j, 0)
                if result:
                    return True

        return result
        