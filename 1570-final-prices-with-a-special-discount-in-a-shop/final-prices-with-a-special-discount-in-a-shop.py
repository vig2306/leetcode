class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = [-1]*len(prices)
        # mini = [-1]*len(prices)
        # mini[-1] = prices[-1]
        # for i in range(len(prices)-2, -1, -1):
            
        # result[-1] = prices[-1]
        # for i in range(len(prices)-2, -1, -1):
        #     mini = min(prices[i], mini)
        #     if mini <= prices[i]:
        #         result[i] = prices[i] - mini
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    result[i] = prices[i] - prices[j]
                    break
            if result[i] == -1:
                result[i] = prices[i]
        return result        