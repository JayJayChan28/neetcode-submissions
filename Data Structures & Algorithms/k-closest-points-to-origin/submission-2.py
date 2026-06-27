class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #calculate distances as we iterate store in tuple (distance, (x, y))
        #use max heap --> store only k elements in heap use distance as value

        max_heap = []
        res = []
        for i in range(len(points)):
            x2, y2 = points[i]
            distance = -((0 - x2)**2 + (0 - y2)**2)
            heapq.heappush(max_heap, [distance, [x2, y2]])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
    
        for val in max_heap:
            res.append(val[1])
        return res

        

        
