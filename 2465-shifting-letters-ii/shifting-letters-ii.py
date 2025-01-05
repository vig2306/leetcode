class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        # 0, 4, 1 = 1, 1, 1, 1, 1, 0, 0, 0, 0, 0
        # 1, 5, 1 = 1, 2, 2, 2, 2, 1, 0, 0, 0, 0
        # 3, 7, 0 = 1, 2, 2, 1, 1, 0, -1, -1, 0, 0

        #Optimal Approach:
        #find the start and end index of the query
        #If the direction is 1 then res[start] += 1 and res[end+1] -= 1
        #If the direction is 0 then res[start] -= 1 and res[end+1] += 1
        #Keep in mind that end+1 will not exist if end == len(s)-1
        #In that case we can keep a last element
        #So res size will be len(s)+1 [0 -> n indexes intstead of n-1]
        #After calculating res compute presum on that so that you will get the final shifts

        res = [0]*(len(s)+1)
        result_str = ''
        for shift in shifts:
            start = shift[0]
            end = shift[1]
            direction = shift[2]
            if direction == 1:
                res[start] += 1
                res[end+1] -= 1
            
            else:
                res[start] -= 1
                res[end+1] += 1
        
        prefix = [res[0]]
        for i in range(1, len(res)):
            next_val = res[i] + prefix[i-1]
            prefix.append(next_val)

        for i in range(len(prefix)-1):
            ascii_val = ord(s[i])
            shift = prefix[i]
            new_ascii = ord('a') + ((ascii_val - ord('a') + shift)%26)
            result_str += chr(new_ascii)
        
        return result_str
       

        #Brute Force -> Iterate through all queries and update all indexes between start and end
        # TC -> O(N^2)
        # SC -> O(N)

        # res = [0]*len(s)
        # new_str = ''
        # for shift in shifts:
        #     start = shift[0]
        #     end = shift[1]
        #     direction = shift[2]
        #     for i in range(start, end+1):
        #         if direction == 1:
        #             res[i] += 1
                
        #         else:
        #             res[i] -= 1
        
        # for i in range(len(res)):
        #     ascii_val = ord(s[i])
        #     shift = res[i]
        #     new_ascii = ord('a') + ((ascii_val - ord('a') + shift)%26)
        #     new_str += chr(new_ascii)
        
        # return new_str

            
            



        