class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if (len(self.small) + len(self.large)) == 1:
            return
        elif self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        print(self.large)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        elif len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        
        

    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 1:
            return -self.small[0]
        elif (len(self.small) + len(self.large)) % 2 == 0:
            return (-self.small[0] + self.large[0]) / 2
        
        