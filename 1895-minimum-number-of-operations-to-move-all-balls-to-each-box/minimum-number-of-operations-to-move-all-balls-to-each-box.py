class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        res = []
        for i in range(len(boxes)):
            moves = 0
            for j in range(i):
                if boxes[j] == '1':
                    moves += abs(j-i)

            for j in range(i+1, len(boxes)):
                if boxes[j] == '1':
                    moves += abs(j-i)
            
            res.append(moves)

        return res

        