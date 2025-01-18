class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        
        for city in flights:
            from_city = city[0]
            to_city = city[1]
            cost = city[2]
            graph[from_city].append((to_city, cost))

        min_cost = float('inf')

        cost = [float('inf')]*(n)
        cost[src] = 0
        
        pq = []
        pq.append((0, 0, src)) #{stops, cost, curr_city}
        heapq.heapify(pq)


        while pq:
            stops, curr_cost, curr_city = heapq.heappop(pq)
            
            for dest in graph[curr_city]:
                
                if curr_cost + dest[1] < cost[dest[0]] and stops<=k:
                    cost[dest[0]] = curr_cost + dest[1]
                    heapq.heappush(pq, (stops+1, curr_cost + dest[1], dest[0]))
        

        return cost[dst] if cost[dst] < float('inf') else -1
                
            



