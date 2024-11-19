class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1 = event1[0].split(":")
        end1 = event1[1].split(":")
        start2 = event2[0].split(":")
        end2 = event2[1].split(":")
        start1Time = int(start1[0])*60+int(start1[1])
        end1Time = int(end1[0])*60+int(end1[1])
        start2Time = int(start2[0])*60+int(start2[1])
        end2Time = int(end2[0])*60+int(end2[1])

        # print(start1Time, end1Time, start2Time, end2Time)

        firstStart = min(start1Time, start2Time)
        if start2Time < start1Time:
            start1Time, start2Time = start2Time, start1Time
            end1Time, end2Time = end2Time, end1Time
        
        # print(start1Time, end1Time, start2Time, end2Time)

        if start2Time > end1Time:
            return False
        
        return True

        