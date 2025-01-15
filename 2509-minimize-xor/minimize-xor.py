class Solution:
    def setBitsArray(self, num):
        res = [0]*32
        for i in range(31, -1, -1):
            if num <= 0:
                break
            rem = num % 2
            res[i] = rem
            num = num //2
        
        return res

    def minimizeXor(self, num1: int, num2: int) -> int:
        if num1 == num2:
            return num1
        
        result = [0]*32
        arr1 = self.setBitsArray(num1)
        arr2 = self.setBitsArray(num2)
        
        num1Count = sum(arr1)
        num2Count = sum(arr2)
        if num1Count == num2Count:
            return num1
        
        i = 0
        while i<32 and num1Count and num2Count:
            if arr1[i] != 1:
                i = i+1
                continue
            
            result[i] = 1
            num2Count -= 1
            num1Count -= 1
            i = i+1
        
        print(num1Count, num2Count)
        # while i< 32 and num1Count:
        #     if arr1[i] == 1:
        #         result[i] = 1
        #         num1Count -=1
            
        #     i = i+1
        j = i
        i= 31
        while num2Count:
            if arr1[i] == 0:
                result[i] = 1
                num2Count -= 1
            i = i-1
        
        final_res = 0
        for i in range(31, -1, -1):
            final_res += result[i]*(2**(31-i))
        
        return final_res

            

            

            

        






        return 0
        # 0011
        # 0101
        # 0011 ^ x = min
        # setBits of num1 = setBits of num 2 -> return 0
        # setBits of num1 > setBits of num 2

        # 1110
        # 0011
        # 1100


        # 0001
        # 1110
        # 0111





        