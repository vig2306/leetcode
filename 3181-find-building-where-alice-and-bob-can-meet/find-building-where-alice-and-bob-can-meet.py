class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        result = [-1]*len(queries)
        query_index_map = defaultdict(list)
        for i in range(len(queries)):
            a = queries[i][0]
            b = queries[i][1]
            if a > b:
                a,b = b,a

            if a == b or heights[a] < heights[b]:
                result[i] = b
            
            else:
                h = max(heights[a], heights[b])
                query_index_map[b].append((h, i))
        
        min_heap = []
        for i, h in enumerate(heights):
            
            while min_heap and min_heap[0][0] < h:
                less_height, res_index = heapq.heappop(min_heap)
                result[res_index] = i
            
            for query in query_index_map[i]:
                heapq.heappush(min_heap, query)
        
        return result

        # index_jump = [-1]*len(heights)
        # stack = []
        # for i in range(len(heights)):
        #     while stack and stack[-1][0] < heights[i]:
        #         value, index = stack.pop()
        #         index_jump[index] = i
            
        #     stack.append((heights[i], i))
        # result = []

        # for query in queries:
        #     a, b = query[0], query[1]
        #     if a > b:
        #         a, b = b, a
            
        #     if a == b or heights[a] < heights[b]:
        #         result.append(b)
        #         continue
        #     else:

        #         while heights[a] >= heights[b]:
        #             new_index = index_jump[b]
        #             if new_index == -1:
        #                 break
        #             b = new_index
            
        #     if heights[a] < heights[b]:
        #         result.append(b)
        #     else:
        #         result.append(-1)
        
        
        # return result

        

        