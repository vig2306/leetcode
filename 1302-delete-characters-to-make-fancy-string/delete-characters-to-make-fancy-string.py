class Solution:
    def makeFancyString(self, s: str) -> str:

        prev_char = None
        result = ''
        count = 0

        
        for i in range(len(s)):
            if i == 0:
                prev_char = s[i]
                result += s[i]
                count += 1
                continue
            
            if s[i] == prev_char:
                count += 1
                if count > 2:
                    continue
                else:
                    result += s[i]
            else:
                prev_char = s[i]
                result += s[i]
                count = 1
        
        return result

        