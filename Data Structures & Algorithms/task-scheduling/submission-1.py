class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Use max_heap, process the most frequent value first
        #FIFO, we want to store the number of cycles before we can process it again
        #use queue data structure
        #use max_heap structure --> insert into 

        count = Counter(tasks)
        q = deque()
        time = 0

        #creates the max heap
        maxHeap = [-n for n in count.values()]
        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1
            #if maxheap not empty
            if maxHeap:
                freq = 1 + heapq.heappop(maxHeap)
                if freq:
                    q.append((freq, time + n))
            #if the time == idle time
            if q and q[0][1] == time:
                #we only need the freq for the max_heap
                heapq.heappush(maxHeap, q.popleft()[0])
        return time





