class Solution:
    def maxScore(self, s: str) -> int:
        count_zeroes_left = 0
        count_ones_left = 0
        count_zeroes_right = 0
        count_ones_right = 0
        max_score = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                count_zeroes_left += 1
            if s[i] == '1':
                count_ones_left += 1
            
            for j in range(i+1,len(s)):
                if s[j] == '0':
                    count_zeroes_right += 1
                if s[j] == '1':
                    count_ones_right += 1
            

            curr_score = count_zeroes_left + count_ones_right
            max_score = max(max_score, curr_score)
            count_zeroes_right = 0
            count_ones_right = 0
        
        return max_score




        