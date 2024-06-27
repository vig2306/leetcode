class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first = edges[0][0]
        second = edges[0][1]
        third = edges[1][0]
        fourth = edges[1][1]
        
        if first == third or first == fourth:
            return first
        
        if second == third or second == fourth:
            return second
            

        