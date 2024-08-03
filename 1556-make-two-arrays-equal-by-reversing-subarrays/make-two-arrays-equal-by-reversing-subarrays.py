class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_set = {}
        arr_set = {}
        n = len(target)
        for i in range(n):
            target_set[target[i]] = target_set.get(target[i], 0) + 1
            arr_set[arr[i]] = arr_set.get(arr[i], 0) + 1
        
        for key in target_set:
            if key not in arr_set or arr_set[key] != target_set[key]:
                return False
        
        for key in arr_set:
            if key not in target_set or target_set[key] != arr_set[key]:
                return False

        return True
        