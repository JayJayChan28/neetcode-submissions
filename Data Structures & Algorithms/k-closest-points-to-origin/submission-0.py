class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x2, y2 = 0, 0
        map_distances = {}
        distances = []
        res = []
        for point in points:
            x1, y1 = point[0], point[1]
            distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            distances.append([distance, point])
        #min heap
        heapq.heapify(distances)
        #get k smallest points
        for _ in range(k):
            distance, point = heapq.heappop(distances)
            res.append(point)
        return res