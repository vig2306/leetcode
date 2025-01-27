class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree = [0]*numCourses
        reachable = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        for pre in prerequisites:
            a, b = pre[0], pre[1]
            reachable[a][b] = True
        
        for middle in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if i != j and reachable[i][j] == False:
                        if reachable[i][middle] == True and reachable[middle][j] == True:
                            reachable[i][j] = True
        

        res = []
        for query in queries:
            a, b = query[0], query[1]
            if reachable[a][b] == True:
                res.append(True)
            else:
                res.append(False)

        return res





