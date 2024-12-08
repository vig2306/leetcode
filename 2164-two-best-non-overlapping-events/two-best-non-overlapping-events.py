class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        minHeap = []
        events.sort()
        maxVal = 0
        prevMax = 0
        for i in range(len(events)):
            while minHeap and events[i][0] > minHeap[0][0]:
                currEnd, currVal = heapq.heappop(minHeap)
                prevMax = max(prevMax, currVal)
            
            maxVal = max(maxVal, events[i][2] + prevMax)
            heapq.heappush(minHeap, (events[i][1], events[i][2]))
        

        return maxVal

        # endTime = []
        # maxendTime = 0
        # for i in range(len(events)):
        #     maxendTime = max(events[i][1], maxendTime)
        
        # for i in range(maxendTime):
        #     endTime.append(0)
        
        # print(endTime)

        