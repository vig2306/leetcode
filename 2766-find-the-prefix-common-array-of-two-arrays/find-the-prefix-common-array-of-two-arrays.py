class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = [0]*len(A)
        seen_A = set()
        seen_B = set()
        if A[0] == B[0]:
            result[0] = 1
        seen_A.add(A[0])
        seen_B.add(B[0])
            
        for i in range(1, len(A)):
            if A[i] == B[i]:
                result[i] = result[i-1] + 1
                seen_A.add(A[i])
                seen_B.add(B[i])
                continue
            result[i] = result[i-1]
            if A[i] in seen_B:
                result[i] += 1
            if B[i] in seen_A:
                result[i] += 1
            seen_A.add(A[i])
            seen_B.add(B[i])
        
        return result
        



        
        