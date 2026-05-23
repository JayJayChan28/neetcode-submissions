class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            values = None
            while stack and stack[-1][0] < temperatures[i]:
                values = stack.pop()
                curr_day = values[1]
                day_diff = i - curr_day
                res[curr_day] = day_diff

            stack.append((temperatures[i], i))
        return res


            






