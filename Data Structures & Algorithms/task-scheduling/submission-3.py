class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #calculate freq
        freq_map = Counter(tasks)
        max_heap = [-n for n in freq_map.values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0
        while q or max_heap:
            if q and q[0][0] == time:
                heapq.heappush(max_heap, q.popleft()[1])
            if not max_heap:
                time += 1
                continue
            freq = heapq.heappop(max_heap) + 1
            time += 1
            idletime = time + n
            if freq != 0:
                q.append([idletime, freq])
        return time




        