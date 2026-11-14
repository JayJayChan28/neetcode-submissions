class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #use min heap sturcuture
        #SORT BOTH so that queries oinly increase
        #store range values, and their end values, append into res = [] take first value of min heap
        #create nhew heap for teach iteration

        min_heap = []

        intervals.sort(key = lambda x: x[0])
        interval_pointer = 0
        res = {}
        for val in sorted(queries):
            while interval_pointer < len(intervals) and intervals[interval_pointer][0] <= val:
                #(len, end)
                heapq.heappush(min_heap, (intervals[interval_pointer][1] - intervals[interval_pointer][0] + 1, intervals[interval_pointer][1]))
                interval_pointer += 1
            #if val greater than end val we remove from heap
            while min_heap and val > min_heap[0][1]:
                heapq.heappop(min_heap)
            #smallest len of explored query 
            res[val] = min_heap[0][0] if min_heap else -1
        return [res[q] for q in queries]
            