class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start_i = i
            while stack and h < stack[-1][1]:
                start_i, curr_height = stack.pop()
                max_area = max(max_area, curr_height * (i - start_i))
            stack.append((start_i, h))
        
        while stack:
            i, h = stack.pop()
            max_area = max(max_area, h * (len(heights) - i))
        return max_area