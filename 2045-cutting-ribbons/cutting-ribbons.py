class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        high = max(ribbons)
        low = 1
        max_len = 0
        while low <= high:
            mid = (low+high) // 2
            count = 0
            for i in range(len(ribbons)):
                count += ribbons[i]//mid
            
            if count >= k:
                max_len = max(mid, max_len)
                low = mid + 1
            
            else:
                high = mid-1
            
        return max_len

        