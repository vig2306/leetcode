class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        res = 0
        for bit in derived:
            res ^= bit
        
        return True if res == 0 else False

    



        