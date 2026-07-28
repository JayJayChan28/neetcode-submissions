class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, subset, total):
            #base case
            if total > target or i >= len(nums):
                return
            elif total == target:
                res.append(subset.copy())
                return
            #constraint

            subset.append(nums[i])
            dfs(i, subset, total + nums[i])
            subset.pop()
            dfs(i + 1, subset, total)
        dfs(0, subset, 0)
        return res

