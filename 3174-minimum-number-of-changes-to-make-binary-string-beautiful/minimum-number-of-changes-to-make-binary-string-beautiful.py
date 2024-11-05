class Solution:
    def minChanges(self, s: str) -> int:
        block = []
        inversion = 0
        for i in range(0,len(s),2):
            if s[i] != s[i+1]:
                inversion +=1
        
        return inversion


            

        