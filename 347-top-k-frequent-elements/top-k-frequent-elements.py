class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''Brute Force: Go through array, store in hashmap, sort by value
            find the top k frequent elements
            TC-> O(NLogn)
            SC ->O(N)
            '''
        
        countDict = {}
        for i in range(len(nums)):
            countDict[nums[i]] = countDict.get(nums[i], 0) + 1
        
        frequencyList = sorted(countDict.items(), key=lambda item: item[1], reverse=True)
        
        return [frequencyList[i][0] for i in range(k)]
        




        