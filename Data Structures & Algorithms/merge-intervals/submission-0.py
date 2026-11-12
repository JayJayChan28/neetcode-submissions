class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort then conider three mrege cases
        #curr_val_start < prev_val_end:
        #or
        #prev_val_end > curr_val_start
        #append to res

        intervals.sort(key = lambda x:x[0])

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            #first case: prev_val_end > curr_val_start <-- we know not overlap
            if res[-1][1] < intervals[i][0]:
                #append the interval
                res.append(intervals[i])
            elif intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])

        return res


            