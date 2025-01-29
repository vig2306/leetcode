class Solution:
    #Topo sort Approach:
    #Keep on removing nodes with degree as 1
    #there is no indegree in this both nodes will have degree as 1
    #At the end when there is degree as 2 for nodes that will be part of cycle
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        vertices = len(edges)
        graph = [[] for _ in range(vertices)]
        degree = [0]*(vertices)
        for edge in edges:
            a = edge[0]
            b = edge[1]
            degree[a-1] += 1
            degree[b-1] += 1
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        
        queue = deque()
        
        
        for i in range(len(degree)):
            if degree[i] == 1:
                queue.append(i)
                
        
        while queue:
            curr_node = queue.popleft()
            for adj in graph[curr_node]:
                degree[adj] -= 1
                if degree[adj] == 1:
                    queue.append(adj)
        
        res = [-1,-1]
        for i in range(len(edges)-1,-1,-1):
            a = edges[i][0]
            b = edges[i][1]
            if degree[a-1] == 2 and degree[b-1] == 2:
                res[0] = a
                res[1] = b
                break
        
        return res



    # def dfs(self, node, parent, path):
    #     self.visited.add(node)
    #     for neighbor in self.graph[node]:
    #         if neighbor not in self.visited:
    #             path.append(neighbor)
    #             if self.dfs(neighbor, node, path):
    #                 return True
                
    #         else:
    #             if neighbor != parent:
    #                 path.append(neighbor)
    #                 self.cycle = path.copy()
    #                 return True
            
    #     path.pop()
        
    #     return False

    # def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    #     self.graph = defaultdict(list)
    #     for u,v in edges:
    #         self.graph[u].append(v)
    #         self.graph[v].append(u)

    #     self.cycle = []
    #     self.visited = set()
    #     self.dfs(1, -1, [1])
    #     nodes = set()
    #     for i in range(len(self.cycle)-1):
    #         a = self.cycle[i]
    #         b = self.cycle[i+1]
    #         nodes.add((a,b))
        
    #     print(self.cycle)
    #     print(nodes)

    #     for i in range(len(edges)-1, -1, -1):
    #         a = edges[i][0]
    #         b = edges[i][1]
    #         if (a,b) in nodes or (b,a) in nodes:
    #             return [a,b]


            
            
                

                
