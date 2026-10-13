class Solution:
    def climbStairs(self, n: int) -> int:
        #bottom up apporach

        #summ the prev val? two pointers 
        summed = 0
        top, bot = 0, 1
        for _ in range(n):
            total_new = top + bot
            top = bot
            bot = total_new
            summed = total_new
        return summed
