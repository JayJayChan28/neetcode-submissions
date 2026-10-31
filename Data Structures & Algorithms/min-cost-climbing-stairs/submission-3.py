class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_1 = 0
        prev_2 = 0

        for i in range(len(cost)):
            curr = cost[i] + min(prev_1, prev_2)
            prev_2 = prev_1
            prev_1 = curr
        
        return min(prev_1, prev_2)



