class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = {}
        for i in range(len(arr)):
            hashmap[arr[i]] = hashmap.get(arr[i], 0) + 1
        
        i = 1
        for key in hashmap:
            if hashmap[key] == 1:

                if k == i:
                    return key
                else:
                    i = i+1
    
        
        return ""


            
        