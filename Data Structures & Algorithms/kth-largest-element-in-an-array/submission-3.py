class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #max heap? kth largerest. pop k times?

        #o(n) time
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
        #minimum among the kth largest elements, think window of k of the largest values minim of that is the kth largest
        return heap[0]