class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''Better: Keep minHeap of size K and then find the topK in Dictionary 
        instead of sorting
        TC -> O(NLogk)
        SC -> O(N)'''
        countDict = {}
        for i in range(len(nums)):
            countDict[nums[i]] = countDict.get(nums[i], 0) + 1
        
        minHeap = []
        for key, value in countDict.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap, (value, key))
            
            else:
                if value >= minHeap[0][0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (value, key))
        res = []
        while minHeap:
            key, value = heapq.heappop(minHeap)
            res.append(value)
        return res

                
            

        '''Brute Force: Go through array, store in hashmap, sort by value
            find the top k frequent elements
            TC-> O(NLogn)
            SC ->O(N)
            '''
        
        countDict = {}
        for i in range(len(nums)):
            countDict[nums[i]] = countDict.get(nums[i], 0) + 1
        
        frequencyList = sorted(countDict.items(), key=lambda item: item[1], reverse=True)
        
        return [frequencyList[i][0] for i in range(k)]
        




        