class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = [-1]*len(prices)
        stack = []
        for i in range(0, len(prices)):
            curr_val = prices[i]

            while stack and curr_val <= stack[-1][0]:
                top, index = stack.pop()
                result[index] = top - curr_val
            
            stack.append((curr_val, i))
        
        while stack:
            top, index = stack.pop()
            result[index] = top
        
        return result



        #Brute Force
        #TC -> O(N^2)
        #SC -> O(N)
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] <= prices[i]:
        #             result[i] = prices[i] - prices[j]
        #             break
        #     if result[i] == -1:
        #         result[i] = prices[i]
        # return result        