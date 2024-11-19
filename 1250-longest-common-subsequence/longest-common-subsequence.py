class Solution:
    def recursion(self, text1, text2, ind1, ind2):
        if ind1 < 0 or ind2 < 0:
            return 0
        
        if self.memo[ind1][ind2] != -1:
            return self.memo[ind1][ind2]
        ans = 0
        if text1[ind1] == text2[ind2]:
            ans = 1 + self.recursion(text1,text2,ind1-1,ind2-1)
        
        else:
            a = self.recursion(text1,text2,ind1,ind2-1)
            b = self.recursion(text1,text2,ind1-1,ind2)
            ans = max(a,b)
        self.memo[ind1][ind2] = ans
        return ans

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        self.memo = []
        for i in range(len(text1)):
            temp = []
            for j in range(len(text2)):
                temp.append(-1)
            self.memo.append(temp)
        
        ind1 = len(text1) - 1
        ind2 = len(text2) - 1
        return self.recursion(text1, text2, ind1, ind2)
        