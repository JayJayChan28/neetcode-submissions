class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        rate = (l + r) // 2
        min_rate = r
        while l < r:
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / float(rate))
            if hours <= h:
                min_rate = min(min_rate, rate)
            if hours > h:
                l = rate + 1
            elif hours <= h:
                r = rate 
            rate = (l + r) // 2
        return min_rate


            