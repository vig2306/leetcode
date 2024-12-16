class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        #Updating nums array during K iterations:
        min_heap = []
        for i in range(len(nums)):
            min_heap.append((nums[i], i))
        
        heapq.heapify(min_heap)
        while k:
            min_value, index = heapq.heappop(min_heap)
            nums[index] = nums[index] * multiplier
            heapq.heappush(min_heap, (nums[index], index))
            k -= 1
        
        return nums

        #Popping of elements of heap at the end and updating (Extra While Loop)
        # min_heap = []
        # for i in range(len(nums)):
        #     min_heap.append((nums[i], i))
        
        # heapq.heapify(min_heap)
        # while k:
        #     min_value, index = heapq.heappop(min_heap)
        #     new_value = min_value * multiplier
        #     heapq.heappush(min_heap, (new_value, index))
        #     k -= 1
        
        # while min_heap:
        #     value, index = heapq.heappop(min_heap)
        #     nums[index] = value
        
        # return nums
        