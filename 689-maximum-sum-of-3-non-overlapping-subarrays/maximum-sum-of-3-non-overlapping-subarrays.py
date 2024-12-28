class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Number of possible subarray starting positions
        n = len(nums) - k + 1

        # Calculate sum of all possible k-length subarrays
        sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            sums.append(sums[-1] - nums[i - k] + nums[i])

        # memo[i][j]: max sum possible starting from index i with j subarrays remaining
        memo = [[-1] * 4 for _ in range(n)]
        indices = []

        # First find optimal sum using DP
        self._dp(sums, k, 0, 3, memo)

        # Then reconstruct the path to find indices
        self._dfs(sums, k, 0, 3, memo, indices)

        return indices

    def _dp(self, sums, k, idx, rem, memo):
        if rem == 0:
            return 0
        if idx >= len(sums):
            return float("-inf") if rem > 0 else 0

        if memo[idx][rem] != -1:
            return memo[idx][rem]

        # Try taking current subarray vs skipping it
        with_current = sums[idx] + self._dp(sums, k, idx + k, rem - 1, memo)
        skip_current = self._dp(sums, k, idx + 1, rem, memo)

        memo[idx][rem] = max(with_current, skip_current)
        return memo[idx][rem]

    def _dfs(self, sums, k, idx, rem, memo, indices):
        if rem == 0 or idx >= len(sums):
            return

        with_current = sums[idx] + self._dp(sums, k, idx + k, rem - 1, memo)
        skip_current = self._dp(sums, k, idx + 1, rem, memo)

        # Choose path that gave optimal result in DP
        if with_current >= skip_current:  # Take current subarray
            indices.append(idx)
            self._dfs(sums, k, idx + k, rem - 1, memo, indices)
        else:  # Skip current subarray
            self._dfs(sums, k, idx + 1, rem, memo, indices)




    # def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:        

    #     #Brute Force: Vahiyad
    #     #TC -> Possibly O(N^3)
    #     #SC -> O(N)
    #     min_heap = []
    #     prefix = [0]
    #     for i in range(len(nums)):
    #         curr_sum = prefix[i] + nums[i]
    #         prefix.append(curr_sum)
        
    #     left = 0
    #     right = 0
    #     max_sum = float('-inf')
    #     i = 0
    #     while i < len(prefix):
    #         j = i + k
    #         if j >= len(prefix):
    #             break
    #         first_sum = prefix[j] - prefix[i]

    #         while j < len(prefix):
    #             l = j + k
    #             if l >= len(prefix):
    #                 break
    #             second_sum = prefix[l] - prefix[j]

    #             while l < len(prefix):
    #                 if l+k >= len(prefix):
    #                     break
    #                 third_sum = prefix[l+k] - prefix[l]
    #                 total_sum = first_sum + second_sum + third_sum
    #                 if total_sum > max_sum:
    #                     max_sum = total_sum
    #                     while min_heap:
    #                         ni, nj, nl = heapq.heappop(min_heap)
    #                     heapq.heappush(min_heap, (i,j,l))
    #                 if total_sum == max_sum:
    #                     if (i,j,l) < min_heap[0]:
    #                         heapq.heappop(min_heap)
    #                         heapq.heappush(min_heap, (i,j,l))
    #                 l = l+1
    #             j = j +1
    #         i = i+1
        
        
    #     return list(min_heap[0])



        