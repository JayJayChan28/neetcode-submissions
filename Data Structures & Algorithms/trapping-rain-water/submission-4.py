class Solution:
    def trap(self, height: List[int]) -> int:
        #lets do two poiter technique
        #take advantage taht we know the smaller of the two l and r will be bottle neck 

        #min(maxL, maxR) <-- find or bottle neck and calculate teh curr ith index
        #
        if not height:
            return 0
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        total = 0
        while l <= r:
            if maxL <= maxR:
                trapped_water_ith = maxL - height[l] if maxL - height[l] > 0 else 0
                maxL = max(maxL, height[l])
                l += 1
            else:
                trapped_water_ith = maxR - height[r] if maxR - height[r] > 0 else 0
                maxR = max(maxR, height[r])
                r -= 1
            
            total += trapped_water_ith
        return total
        
            