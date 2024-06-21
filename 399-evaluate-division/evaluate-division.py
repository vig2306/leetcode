class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # queue = []

        # def dfs(curr_node, end_node, adj, visited, path):
        #     visited[curr_node] = True
        #     path.append(curr_node)
        #     ans = 1.0
        #     if curr_node == end_node:
        #         return ans
            
        #     else:
        #         for i in adj[curr_node]:
        #             if i not in visited.keys():
        #                 ans = i[1] * dfs(i, end_node, adj, visited, path)

        # def dfs(node, end_node, graph, visited):
        #     if node == end_node:
        #         return 1.0

        #     if node not in visited:
        #         print (node)
        #         visited.add(node)
        #         for neighbour in graph[node]:
        #             print(neighbour)
        #             if neighbour[0] in visited:
        #                 continue
        #             ans = neighbour[1] * dfs(neighbour[0], end_node, graph, visited)
        
        def bfs(start_node, end_node, adj):
            visited = set()
            q = []
            q.append([start_node, 1])
            visited.add(start_node)

            while q:
                curr, curr_weight = q.pop(0)
                if curr == end_node:
                    return curr_weight
                
                for neighbor in adj[curr]:
                    if neighbor[0] not in visited:
                        q.append((neighbor[0], curr_weight * neighbor[1]))
                        visited.add(neighbor[0])
            
            return -1
            

        adj = {}
        for i in range(len(equations)):
            adj[equations[i][0]] = []
            adj[equations[i][1]] = []
        
        for i in range(len(equations)):
            temp = (equations[i][1], values[i])
            temp2 = (equations[i][0], 1/values[i])
            adj[equations[i][0]].append(temp)
            adj[equations[i][1]].append(temp2)
        
        # for vertex, neighbors in adj.items():
        #     print(f"{vertex} -> {' '.join(map(str, neighbors))}")
        print(adj)
        result = []
        for i in range(len(queries)):
            path = []
            ans = 0
            if queries[i][0] == queries[i][1]:
                if queries[i][0] not in adj.keys():
                    result.append(-1.0)
                else:
                    result.append(1.0)
            
            else:
                if queries[i][0] not in adj.keys() or queries[i][1] not in adj.keys():
                    print(queries[i][0], "->", queries[i][1], " I am here")
                    result.append(-1.0)
                
                else:
                    ans = bfs(queries[i][0], queries[i][1], adj)
                    result.append(ans)


        return result


        


        