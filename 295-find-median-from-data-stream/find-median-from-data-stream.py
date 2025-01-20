class MedianFinder:
    def __init__(self):
        self.largeHeap = []
        heapq.heapify(self.largeHeap)
        self.smallHeap = []
        heapq.heapify(self.smallHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -num)
        if self.largeHeap and self.smallHeap and self.largeHeap[0] < -(self.smallHeap[0]):
                val = heapq.heappop(self.smallHeap)
                heapq.heappush(self.largeHeap, -val)
        
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -val)

        if len(self.largeHeap) > len(self.smallHeap) + 1:
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -val)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -self.smallHeap[0]

        elif len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]

        return (self.largeHeap[0] - self.smallHeap[0]) / 2


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()