class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        result = []
        freq_map = []
        curr = []

        for i in range(0, len(s)):
            curr_char_idx = ord(s[i]) - ord('a')
            if not freq_map:
                f1 = [0]*26
                f1[curr_char_idx] += 1
                freq_map.append(f1)
            else:
                f1 = freq_map[-1].copy()
                f1[curr_char_idx] += 1
                freq_map.append(f1)
            
        # print(freq_map)

        for query in queries:
            start, end = query[0], query[1]
            count = 0
            # print(query)

            curr_freq_map = [0 for _ in range(26)]
            for k in range(26):
                if start == 0:
                    curr_freq_map[k] = freq_map[end][k]
                    continue
                curr_freq_map[k] = freq_map[end][k] - freq_map[start-1][k]

            for j in range(0, 26):
                n = curr_freq_map[j]
                if n > 0:
                    if n == 1:
                        count += n
                    else:
                        count += n + (n * (n - 1))//2

            result.append(count)
        
        return result


        