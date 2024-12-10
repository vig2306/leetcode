class Solution:
    def maximumLength(self, s: str) -> int:
        left = 0
        right = 0
        hashmap = {}
        curr_char = s[left]
        window_size = 0
        while right <= len(s):
            if right == len(s) or s[right] != curr_char:
                window_size = right - left
                key = curr_char
                for i in range(window_size):
                    hashmap[curr_char] = hashmap.get(curr_char, 0) + (window_size-i)
                    curr_char = curr_char + key

                left = right
                if left == len(s):
                    break
                curr_char = s[left]
            else:
                right = right + 1


        print(hashmap)
        max_len = -1
        for k, v in hashmap.items():
            if v >= 3:
                max_len = max(len(k), max_len)

        return max_len




        
        
        