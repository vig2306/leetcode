class Solution:
    def minimumLength(self, s: str) -> int:
        char_count = {}
        for ch in s:
            if ch in char_count:
                char_count[ch] += 1
            else:
                char_count[ch] = 1
        
        total_count = 0
        for ch, count in char_count.items():
            if count % 2 == 0:
                new_count = 2
            else:
                new_count = 1
            char_count[ch] = new_count
            total_count += new_count
        
        return total_count
                



        