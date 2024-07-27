class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        graph = []
        c=0
        inf = float('inf')
        for i in range(26):
            graph.append([])
            for j in range(26):
                if i==j:
                    graph[i].append(0)
                    continue
                graph[i].append(inf)
        
        # print(ord('a'))
        # print(ord('z'))
        
        for k in range(len(cost)):
            i = ord(original[k]) - 97
            # print(i)
            j = ord(changed[k]) - 97
            # print(j)
            graph[i][j] = min(graph[i][j], cost[k])

        # print(graph)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        change_cost = 0
        for i in range(len(source)):
            source_index = ord(source[i]) - 97
            target_index = ord(target[i]) - 97
            change_cost = change_cost + graph[source_index][target_index]
            if change_cost == inf:
                change_cost = -1
                break

            

        return change_cost




        