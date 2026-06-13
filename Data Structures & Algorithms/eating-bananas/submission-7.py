class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #set range of rates from 1 to max(piles)
        #run binary search, if time for mid rate > h increase rate w/ l = mid + 1
        #vise versa for other
        #ensure to capture edge case, when midrate == h shift r = mid + 1
        #we want the smalles rate so we check al the samlelr valeus


        eating_rates = range(1, max(piles) + 1)
        l, r = 0, len(eating_rates) - 1
        res = float("inf")

        while l <= r:
            mid_rate_index = (l + r) // 2
            rate_of_consumption = eating_rates[mid_rate_index]
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/rate_of_consumption)
                print(pile/rate_of_consumption)
            print(total_time)
            if total_time <= h:
                r = mid_rate_index - 1
                res = min(res, rate_of_consumption)
            else:
                l = mid_rate_index + 1
        return res

                
