class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, interval in enumerate(intervals):
            #if end of new interval is less than start of current interval we know that it is before the current interval
            if interval[0] > newInterval[1]:
                res.append(newInterval)
                #since it is sorted we know that rest of it will be the remaining value of the interval
                return res + intervals[i:]
            
            #know that the new interval comes after
            elif newInterval[0] > interval[1]:
                res.append(interval)

            else:

                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        res.append(newInterval)
        
        return res