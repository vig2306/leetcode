class Solution:
    def recursion(self, index, n, digits, temp):
        if index == n:
            self.result.append(temp)
            return
        

        for char in self.number_map[digits[index]]:
            self.recursion(index+1, n, digits, temp+char)
        
        return
 
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        self.result = []
        n = len(digits)
        self.number_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        self.recursion(0, n, digits, '')

        return self.result



        # def recur(i, n):
        #     if i == n-1:
        #         return number_map[digits[i]]
            
        #     final = []
        #     for j in range(len(number_map[digits[i]])):
        #         curr_str = number_map[digits[i]][j]
        #         res = [curr_str + x for x in recur(i+1, n)]
        #         for k in range(len(res)):
        #             final.append(res[k])
            
        #     return final

        # if digits == "":
        #     return result
    
        # result = recur(0, n)
        
        # return result

        