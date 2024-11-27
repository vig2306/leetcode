class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        tcount = {}
        scount = {}
        
        for i in range(len(s)):
            if s[i] in scount:
                scount[s[i]] = scount[s[i]] + 1
            else:
                scount[s[i]] = 1


            if t[i] in tcount:
                tcount[t[i]] = tcount[t[i]] + 1
            else:
                tcount[t[i]] = 1

        
        return True if scount == tcount else False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using a dictionary to map character frequency counts to lists of anagrams
        anagram_groups = defaultdict(list)
        
        # Process each string in the input list
        for word in strs:
            # Initialize a count array of size 26 for each letter in the alphabet
            # This array represents the frequency of each character in the word
            char_count = [0] * 26
            for char in word:
                # Update the frequency of the character in the count array
                char_count[ord(char) - ord('a')] += 1

            # Use the character count tuple as a key to group anagrams
            anagram_groups[tuple(char_count)].append(word)

        # Return all the grouped anagram lists
        return list(anagram_groups.values())

        # Time Complexity: O(n * k)
        # - n is the number of strings in the input list.
        # - k is the maximum length of a string.
        # - For each string, counting characters takes O(k), and we process n strings.
        # - Thus, the total complexity is O(n * k).

        '''Brute Force -> Iterate through all elements and add the to result if anagrams 
        '''
        # res = []
        # done_str = set()
        # for i in range(len(strs)):
        #     curr_str = strs[i]
        #     if curr_str in done_str:
        #         continue
        #     temp = []
        #     for j in range(i+1, len(strs)):
        #         test_str = strs[j]
        #         if self.isAnagram(curr_str, test_str):
        #             temp.append(test_str)
        #             done_str.add(test_str)
            
        #     temp.append(curr_str)
        #     done_str.add(curr_str)
        #     res.append(temp)
        
        # return res

                



                

        