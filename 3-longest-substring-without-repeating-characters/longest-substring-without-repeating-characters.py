class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        n = len(s)
        longest = 0
        # print(len(s))
        while start < n:
            end = start
            visited = set()
            count = 0
            while end < n:
                if s[end] not in visited:
                    visited.add(s[end])
                    end += 1
                else:
                    break
            longest = max(longest, end-start)
            start = start + 1
        return longest
                

        