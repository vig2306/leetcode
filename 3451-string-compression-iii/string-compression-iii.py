class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''
        count = 0
        for i in range(len(word)):
            if count == 0:
                current_char = word[i]
            
            if word[i] == current_char:
                count = count + 1
                if count > 8:
                    comp = comp + str(count) + word[i]
                    count = 0
                else:
                    continue
            
            else:
                comp = comp + str(count) + current_char
                current_char = word[i]
                count = 1
        if count > 0:
            comp = comp + str(count) + word[-1]
        return comp

        