class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for index, height in enumerate(heights):
            start = index #keeps the index value to compute area
            while stack and stack[-1][1] >= height: # if stack not empty and last val of stack smaller than our curr val
                i, h = stack.pop() # index and height of curr bar
                print(i)
                print(h)
                max_area = max(max_area, (index - i) * h) #calcualtes area 
                start = i
            stack.append((start, height)) #extend left
        print(stack)
        
        #calculate for remaining values in stack

        while stack:
            i, h = stack.pop()
            max_area = max(max_area, (len(heights) - i) * h)
        return max_area