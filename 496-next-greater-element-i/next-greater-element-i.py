class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greatest = -1
        stack = []
        hash_map = {}
        for i in range(len(nums2)-1,-1,-1):
            if not stack:
                stack.append(nums2[i])
                hash_map[nums2[i]] = -1
            else:
                while stack and stack[-1] < nums2[i]:
                    stack.pop()
                if stack:
                    hash_map[nums2[i]] = stack[-1]
                    stack.append(nums2[i])
                else:
                    hash_map[nums2[i]] = -1
                    stack.append(nums2[i])
        res = []
        for num in nums1:
            res.append(hash_map[num])
        
        return res

                

        