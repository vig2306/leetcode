class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []
        for i in range(len(gifts)):
            heapq.heappush(max_heap, -gifts[i])
        
        while k > 0:
            top = -heapq.heappop(max_heap)
            top = int(top**0.5)
            heapq.heappush(max_heap, -top)
            k = k-1
        
        return -(sum(max_heap))

        