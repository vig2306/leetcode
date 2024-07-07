class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        available = numBottles
        empty = 0
        drink = 0
        while available !=0 :
            drink = drink + available
            new_empty = available
            empty = empty + new_empty
    
            available = empty // numExchange
            exchanged = numExchange*available
            empty = empty - exchanged
                
        return drink

        