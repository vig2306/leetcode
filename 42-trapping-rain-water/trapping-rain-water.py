class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lMax = 0
        rMax = 0
        total = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] < lMax:
                    total += lMax - height[left]
                else:
                    lMax = height[left]
                left += 1
            else:
                if height[right] < rMax:
                    total += rMax - height[right]
                else:
                    rMax = height[right]
                right -= 1
        
        return total

        