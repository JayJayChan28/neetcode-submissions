class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        prev_end = intervals[0][1]
        num_remove = 0
        for i in range(1, len(intervals)):
            #if no overlap
            if prev_end <= intervals[i][0]:
                prev_end = intervals[i][1]


            #if prev value greater than start of curent iterval start val
            elif prev_end > intervals[i][0]:
                prev_end = min(prev_end, intervals[i][1])
                num_remove += 1
            
        return num_remove


            