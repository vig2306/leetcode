class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for i in range(len(word)):
            freq[word[i]] = freq.get(word[i], 0) + 1

        sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        print(sorted_freq)
        numbers = 0
        rounds = 1
        pushes = 0 
        for i in range(len(sorted_freq)):
            pushes = pushes + sorted_freq[i][1]*rounds
            numbers = numbers + 1
            if numbers > 7:
                numbers = 0
                rounds += 1
            

        return pushes
        