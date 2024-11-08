class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        n = len(s)
        longest = 0
        visited = set()
        # print(len(s))
        while end < n:
            if s[end] not in visited:
                visited.add(s[end])
                longest = max(longest, end-start+1)
                end += 1          
            else:
                visited.remove(s[start])
                start = start + 1
        return longest
                

        