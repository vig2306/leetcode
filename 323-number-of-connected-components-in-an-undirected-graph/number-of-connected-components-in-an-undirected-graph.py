class Solution:
    def bfs(self, graph, start, visited):
        queue = [start]
        visited[start] = 1
        while queue:
            node = queue.pop()
            for neighbor in graph[node]:
                if visited[neighbor] == 0:
                    queue.append(neighbor)
                    visited[neighbor] = 1
        
        return visited

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for edge in edges:
            a, b = edge[0], edge[1]
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
        