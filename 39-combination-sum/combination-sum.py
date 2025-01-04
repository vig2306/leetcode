class Solution:
    def recursion(self, candidates, target, index, subset):
        if index == -1:
            if target == 0:
                self.result.append(subset.copy())
            return
        
        if target >= candidates[index]:
            subset.append(candidates[index])
            self.recursion(candidates, target-candidates[index], index, subset)
            subset.pop()
        
        self.recursion(candidates, target, index-1, subset)

        return

    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.result = []
        self.recursion(candidates, target, len(candidates)-1, [])

        return self.result

        