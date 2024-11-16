class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []

        for i in range(len(prerequisites)):
            b, a = prerequisites[i][1], prerequisites[i][0]
            graph[b].append(a)

        inDegree = [0] * numCourses
        for course in prerequisites:
            inDegree[course[0]] += 1

        queue = []
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)

        topo = []
        while queue:
            node = queue.pop(0)
            topo.append(node)
            for i in range(len(graph[node])):
                adj = graph[node][i]
                inDegree[adj] -= 1
                if inDegree[adj] == 0:
                    queue.append(adj)
        

        return len(topo) == numCourses
        
