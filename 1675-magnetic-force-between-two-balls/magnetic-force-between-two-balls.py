class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        def checkPlace(arr, dist, m):
            placed = 1
            last_placed = arr[0]
            for i in range(1, len(arr)):

                if arr[i] - last_placed >= dist:
                    placed += 1
                    last_placed = arr[i]
                
                if placed == m:
                    return True
            
            return False
        
        position.sort()
        low = 0
        # high = int((position[-1] / m-1)) + 1
        high = position[-1]
        ans = 0
        if m == len(position):
            print(position)
            max_min_dist = position[1] - position[0]
            for i in range(2,len(position)):
                curr = position[i] - position[i-1]
                max_min_dist = min(max_min_dist, curr)
                
            
            return max_min_dist
        
        while low <= high:
            mid = (low+high)//2
            if checkPlace(position, mid, m):
                ans = mid
                low = mid+1
            else:
                high = mid -1
        
        return ans




        