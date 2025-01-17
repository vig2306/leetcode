class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        indegree = [0]*(numCourses)
        for i in range(numCourses):
            graph[i] = []
        
        for course in prerequisites:
            b = course[1]
            a = course[0]
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        visitedCourses = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                course = queue.pop()
                visitedCourses += 1
                for dependents in graph[course]:
                    indegree[dependents] -= 1
                    if indegree[dependents] == 0:
                        queue.append(dependents)
        
        return True if visitedCourses == numCourses else False


        

        