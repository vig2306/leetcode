class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s = s + s
        # print(s)

        n = len(goal)
        for i in range(len(s)-n+1):
            if s[i:i+n] == goal:
                return True
        
        return False
            
        
        




        