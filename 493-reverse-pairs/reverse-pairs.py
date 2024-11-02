class Solution:

    def reversePairs(self, nums: List[int]) -> int:
    #   Optimal - Merge Sort
    #   TC - O(Nlogn)
    #   SC - O(N)
        def merge(nums, low, mid, high):
            temp = []
            left = low
            right = mid+1

            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
            
            while left<=mid:
                temp.append(nums[left])
                left += 1
            
            while right <= high:
                temp.append(nums[right])
                right += 1

            for i in range(low, high+1):
                nums[i] = temp[i - low]

        def countPairs(nums, low, mid, high):
            count = 0
            right = mid+1
            for i in range(low, mid+1):
                while right <= high and nums[i] > 2*nums[right]:
                    right += 1
                count = count + right - (mid+1)
            return count
                
        def mergeSort(nums, low, high):
            count = 0
            if low >= high:
                return count
            
            mid = (low + high) // 2
            count += mergeSort(nums, low, mid)
            count += mergeSort(nums, mid+1, high)
            count += countPairs(nums, low, mid, high)
            merge(nums, low, mid, high)

            return count
        
        count = mergeSort(nums, 0, len(nums) - 1)
        return count


    # #   Brute Force:
    # #   TC - O(N^2)
    # #   SC - O(1)
    #     result = 0
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] > 2*nums[j]:
    #                 result += 1
        
    #     return result

        
        