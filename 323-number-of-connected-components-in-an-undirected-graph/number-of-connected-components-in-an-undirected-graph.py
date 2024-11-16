class Solution:
    def bfs(self, graph, start, visited):
        queue = [start]
        visited[start] = 1
        while queue:
            node = queue.pop()
            for i in range(len(graph[node])):
                if visited[graph[node][i]] == 0:
                    queue.append(graph[node][i])
                    visited[graph[node][i]] = 1
        
        return visited

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = []
        for i in range(n):
            graph.append([])
        
        for i in range(len(edges)):
            a, b = edges[i][0], edges[i][1]
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [0]*n
        count = 0
        for i in range(len(graph)):
            if visited[i] == 0:
                visited = self.bfs(graph, i, visited)
                # print(self.visited)
                count += 1

        return count
        