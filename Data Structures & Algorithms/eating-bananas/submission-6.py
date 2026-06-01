class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_rate = r

        while l <= r:
            rate = (l + r) // 2

            hours_to_finish = 0
            for pile in piles:
                hours_to_finish += math.ceil(pile / rate)

            if hours_to_finish <= h:
                min_rate = min(min_rate, rate)
                r = rate - 1
            else:
                l = rate + 1

        return min_rate