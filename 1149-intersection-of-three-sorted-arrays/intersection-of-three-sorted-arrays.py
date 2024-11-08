class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        p1, p2, p3 =0,0,0
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] and arr2[p2] == arr3[p3]:
                res.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
                continue
            if arr1[p1] < arr2[p2]:
                p1 += 1
            elif arr2[p2] < arr3[p3]:
                p2 += 1
            else:
                p3+= 1
            
        return res


            


        # freq = {}
        # for i in range(len(arr1)):
        #     freq[arr1[i]] = freq.get(arr1[i], 0) + 1

        # for i in range(len(arr2)):
        #     freq[arr2[i]] = freq.get(arr2[i], 0) + 1

        # for i in range(len(arr3)):
        #     freq[arr3[i]] = freq.get(arr3[i], 0) + 1
        
        # res = []
        # for key, value in freq.items():
        #     if value == 3:
        #         res.append(key)
        # return res