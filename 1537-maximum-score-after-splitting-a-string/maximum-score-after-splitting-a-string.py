class Solution:
    def maxScore(self, s: str) -> int:
        #Sub-Optimal 2: Two-Pass
        #TC -> O(2*N) -> O(N)
        #SC -> O(1)
        max_score = 0
        zeroes = 0
        ones = 0
        for i in range(len(s)):
            if s[i] == '1':
                ones+=1
        
        for i in range(len(s)-1):
            if s[i] == '0':
                zeroes += 1
            if s[i] == '1':
                ones -= 1
            
            max_score = max(max_score, zeroes+ones)
        
        return max_score

        #Sub-Optimal:
        #TC -> O(3*N) -> O(N)
        #SC -> O(2*N) -> O(N)
        #Approach: Find the no of zeroes on the left at each index 
        # and the no of ones on the right at each index
        # max_score = 0
        # zeroes_array = [0]*len(s)
        # ones_array = [0]*len(s)
        # for i in range(len(s)):
        #     if i == 0:
        #         if s[i] == '0':
        #             zeroes_array[i] = 1
        #         continue
        #     if s[i] == '0':
        #         zeroes_array[i] = zeroes_array[i-1] + 1
        #     else:
        #         zeroes_array[i] = zeroes_array[i-1]

        # for i in range(len(s)-1,-1,-1):
        #     if i == len(s)-1:
        #         if s[i] == '1':
        #             ones_array[i] = 1 
        #         continue
        #     if s[i] == '1':
        #         ones_array[i] = ones_array[i+1] + 1
        #     else:
        #         ones_array[i] = ones_array[i+1]
        
        # for i in range(len(zeroes_array)-1):
        #     curr_score = zeroes_array[i] + ones_array[i+1]
        #     max_score = max(curr_score, max_score)
        
        # return max_score


        #Brute Force
        #TC: O(N^2)
        #SC: O(1)
        # count_zeroes_left = 0
        # count_ones_left = 0
        # count_zeroes_right = 0
        # count_ones_right = 0
        # max_score = 0
        # for i in range(len(s)-1):
        #     if s[i] == '0':
        #         count_zeroes_left += 1
        #     if s[i] == '1':
        #         count_ones_left += 1
            
        #     for j in range(i+1,len(s)):
        #         if s[j] == '0':
        #             count_zeroes_right += 1
        #         if s[j] == '1':
        #             count_ones_right += 1
            

        #     curr_score = count_zeroes_left + count_ones_right
        #     max_score = max(max_score, curr_score)
        #     count_zeroes_right = 0
        #     count_ones_right = 0
        
        # return max_score




        