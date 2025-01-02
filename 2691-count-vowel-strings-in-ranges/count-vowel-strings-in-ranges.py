class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        res = []
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowel_set and word[-1] in vowel_set:
                prefix.append(prefix[i]+1)
            else:
                prefix.append(prefix[i])
        
        for query in queries:
            start, end = query[0], query[1]
            number = prefix[end+1] - prefix[start]
            res.append(number)

        return res

        