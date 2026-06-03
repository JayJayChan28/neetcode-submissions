class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and h < stack[-1][1]:
                i_curr, h_curr = stack.pop()
                max_area = max(max_area, (i - i_curr) * h_curr)
                start = i_curr

            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area