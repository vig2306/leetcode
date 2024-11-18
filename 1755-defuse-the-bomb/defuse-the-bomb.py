class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0]*n

        code = code + code
        if k == 0:
            return result
        
        elif k > 0:
            curr_sum = 0
            left = 0
            for right in range(1, len(code)):
                curr_sum = curr_sum + code[right]
                if right-left == k:
                    result[left%n] = curr_sum
                    curr_sum -= code[left+1]
                    left = left + 1
        else:
            curr_sum = 0
            right = len(code) - 1
            for left in range(len(code)-2, -1, -1):
                curr_sum = curr_sum + code[left]
                if left-right == k:
                    result[right%n] = curr_sum
                    curr_sum -= code[right-1]
                    right = right - 1
        
        return result
                    






        