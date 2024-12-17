from collections import deque
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        new_str = ""
        s = sorted(s, reverse=True)
        count = 0
        i = 0
        queue = deque()
        
        while i < len(s):
            if i == 0 or s[i] != new_str[-1]:
                count = 1
                new_str += s[i]
                heap_count = 0
                while queue and heap_count < repeatLimit:
                    if queue:
                        char = queue.popleft()
                        heap_count += 1
                        new_str+=char
                      
            else:
                count += 1
                if count > repeatLimit:
                    queue.append(s[i])
                else:
                    new_str += s[i]
            


            i += 1
        
        return new_str
                    

                

            
        