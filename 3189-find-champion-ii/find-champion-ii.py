class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0]*n
        for edge in edges:
            first = edge[0]
            second = edge[1]
            indegree[second] += 1
        
        count = 0
        ans = 0
        for i in range(n):
            if indegree[i] == 0:
                count+=1
                ans = i
        
        return ans if count == 1 else -1
            
        