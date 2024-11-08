class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        freq = {}
        for i in range(len(arr1)):
            freq[arr1[i]] = freq.get(arr1[i], 0) + 1

        for i in range(len(arr2)):
            freq[arr2[i]] = freq.get(arr2[i], 0) + 1

        for i in range(len(arr3)):
            freq[arr3[i]] = freq.get(arr3[i], 0) + 1
        
        res = []
        for key, value in freq.items():
            if value == 3:
                res.append(key)
        return res
        
        