class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_rate = float('inf')
        while l <= r:
            if l == r:
                return l
            hours_to_finish = 0 
            rate = (l + r) // 2 # rate of eating
            for pile in piles:
                hours_to_finish += math.ceil(pile/rate)
            if hours_to_finish <= h: #decrease the rate to see if there is a smaller one
                r = rate 
                min_rate = min(min_rate, rate)
            elif hours_to_finish > h: # increase the rate to see if we can make the target rate
                l = rate + 1
        return min_rate
            



