class Solution:
    def trap(self, height: List[int]) -> int:
        #two pointer technique
        #l + r pointer
        #take max_l iterate 
        res = 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[0], height[r]

        while l < r:
            min_l_r = min(l_max, r_max)
            if min_l_r == l_max:
                l += 1
                res += (min_l_r - height[l]) if (min_l_r - height[l]) > 0 else 0
                l_max = max(l_max, height[l])
            else:
                r -= 1
                res += (min_l_r - height[r]) if (min_l_r - height[r]) > 0 else 0
                r_max = max(r_max, height[r])
        return res