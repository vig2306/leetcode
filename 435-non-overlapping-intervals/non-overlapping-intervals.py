class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        # print(intervals)
        endTime = 0
        count = 0
        for i in range(len(intervals)):
            if i == 0:
                count += 1
                endTime = intervals[i][1]
                continue
            
            if intervals[i][0] >= endTime:
                count += 1
                endTime = intervals[i][1]

        return len(intervals) - count
        