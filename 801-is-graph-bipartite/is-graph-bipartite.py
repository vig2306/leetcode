class Solution:
    def bfs(self, graph, start):
        queue = [start]
        # visited = [0] * (n)
        self.color[start] = 0
        while queue:
            node = queue.pop(0)
            for i in range(len(graph[node])):
                index = graph[node][i]
                if self.color[index] == -1:
                    self.color[index] = not self.color[node]
                    queue.append(index)
                
                elif self.color[index] == self.color[node]:
                    return False
        
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.color = [-1]*(len(graph))
        for i in range(len(graph)):
            if self.color[i] == -1:
                isBi = self.bfs(graph, i)
                if not isBi:
                    return False
        
        return True


                


        
