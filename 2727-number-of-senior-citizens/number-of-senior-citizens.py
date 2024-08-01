class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0 
        for i in range(len(details)):
            tens = int(details[i][11])
            ones = int(details[i][12])
            age = tens*10 + ones
            if age > 60:
                count+=1
        
        return count
        