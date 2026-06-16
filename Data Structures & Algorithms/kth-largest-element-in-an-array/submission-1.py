class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #max heap? kth largerest. pop k times?

        #o(n) time
        max_heap = [-n for n in nums]
        print(max_heap)
        
        heapq.heapify(max_heap)
        print(max_heap)

        for _ in range(k):
            #log(n) to pop 
            res = heapq.heappop(max_heap)

        return -res