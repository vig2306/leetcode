class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = []
        nodes = set()
        for i in range(len(edges)):
            nodes.add(edges[i][0])
            nodes.add(edges[i][1])
        print(nodes)
        inf = 10**4 + 1

        for i in range(n):
            graph.append([])
            for j in range(n):
                if i==j:
                    graph[i].append(0)
                    continue
                graph[i].append(inf)
        
        # print(graph)
            

        for edge in edges:
            graph[edge[0]][edge[1]] = edge[2]
            graph[edge[1]][edge[0]] = edge[2]
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        print(graph)

        result = []
        for i in range(n):
            count = 0
            for j in range(n):
                if graph[i][j] <= distanceThreshold and graph[i][j] != 0:
                    count+=1
            result.append(count)
        
        ans = -1
        curr_min = n
        for i in range(len(result)):
            if result[i] <= curr_min:
                ans = i
                curr_min = result[i]



        return ans

        
            
            

        