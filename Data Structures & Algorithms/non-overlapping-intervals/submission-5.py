class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda x: x[0])
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            print(prev_end)
            print(intervals[i][0])
            if prev_end > intervals[i][0]:
                #prevend needs to be the smaller of the two
                prev_end = min(prev_end, intervals[i][1])
                res += 1

            #meaning not overlapping, previous end is just end of curent interval
            else:
                prev_end = intervals[i][1]
    
        return res
