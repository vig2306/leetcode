class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        array_ch = [0]*26
        for ch in s:
            index = ord(ch) - ord('a')
            array_ch[index] += 1
        
        odd_count = 0
        for i in range(26):
            if array_ch[i] % 2 != 0:
                odd_count += 1
        
        if odd_count > k:
            return False
        
        return True
        