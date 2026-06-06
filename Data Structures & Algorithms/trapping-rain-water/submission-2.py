class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]
        curr_maxLeft = 0
        maxRight = [0]
        curr_maxRight = 0
        res = 0

        #build max left
        for i in range(len(height) - 1):
            if height[i] > curr_maxLeft:
                maxLeft.append(height[i])
                curr_maxLeft = height[i]
            else:
                maxLeft.append(curr_maxLeft)
    
        #build max_right
        build_right = height[::-1]
        for i in range(len(height) - 1):
            print(build_right[i])
            if build_right[i] > curr_maxRight:
                maxRight.append(build_right[i])
                curr_maxRight = build_right[i]
            else:
                maxRight.append(curr_maxRight)
        maxRight = maxRight[::-1]
        print(maxLeft)
        print(maxRight)


        for i in range(len(height) - 1):
            left = maxLeft[i]
            right = maxRight[i]
            trapped_water = min(left, right) - height[i]
            if trapped_water > 0:
                res += trapped_water
            
        return res

