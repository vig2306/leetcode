class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        min_array = [float('inf')]*(len(arr)+1)
        max_array = [-1]*(len(arr)+1)
        for i in range(len(arr)):
            if i == 0:
                max_array[i+1] = arr[i]
            else:
                max_array[i+1] = max(max_array[i], arr[i])
        
        for i in range(len(arr)-1, -1, -1):
            if i == len(arr)-1:
                min_array[i] = arr[i]
            else:
                min_array[i] = min(min_array[i+1], arr[i])
        
        count = 0
        for i in range(1, len(max_array)-1):
            if max_array[i] <= min_array[i]:
                count += 1
        
        

        return count + 1

        