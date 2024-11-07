class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        hash_map = {}
        max_count = [0]*32
        for i in range(len(candidates)):
            if candidates[i] in hash_map:
                continue
            curr = [0]*32
            curr_num = candidates[i]
            j = 0
            n = len(curr)
            while curr_num > 0:
                rem = curr_num % 2
                curr[n-j-1] = rem
                curr_num = curr_num // 2
                j = j + 1
            hash_map[candidates[i]] = curr
        
        for i in range(len(candidates)):
            curr_num = candidates[i]
            for j in range(len(hash_map[curr_num])):
                max_count[j] += hash_map[curr_num][j]                
        
        return max(max_count)

            

        