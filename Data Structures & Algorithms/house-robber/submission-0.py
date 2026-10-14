from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache 
        def dfs(i):
            if i >= len(nums):
                return 0
#nums[i] + dfs(i + 2) <-- means we robbed house so we add to our max
            return max(nums[i] + dfs(i + 2), dfs(i + 1))
        
        return dfs(0)
