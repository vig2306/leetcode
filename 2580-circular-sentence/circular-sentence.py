class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        final_last_char = sentence[-1]
        first_first_char = sentence[0]

        if first_first_char != final_last_char:
            return False
        

        for i in range(len(sentence)):
            if sentence[i] == " " and sentence[i+1] != sentence[i-1]:
                return False
        
        return True

        