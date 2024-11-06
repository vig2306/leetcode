class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        result = 0
        prev_min = float('inf')
        curr_max = target[0]
        i = 1
        curr_min = target[0]

        while i <= len(target):
            while i < len(target) and target[i] <= target[i-1]:
                # curr_max = max(curr_max, target[i])
                i += 1
            
            if prev_min == float('inf'):
                result += curr_max
            else:
                result += curr_max - prev_min
            if i >= len(target):
                break
            prev_min = target[i-1]
            curr_max = target[i]
            i+=1

        return result



            

        