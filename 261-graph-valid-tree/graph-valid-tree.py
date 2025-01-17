class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = [[] for _ in range(n)]
        for edge in edges:
            a, b = edge[0], edge[1]
            graph[a].append(b)
            graph[b].append(a)
        
        queue = deque()
        queue.append(0)
        visited = set()
        visited.add(0)
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    queue.append(neighbor)
 
        return True if len(visited) == n else False





        