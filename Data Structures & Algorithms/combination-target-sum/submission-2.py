class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #backtracking 
        #base case: i >= len(nums)
        #contraint: total == target --> append subset into res
        #condition: dfs(i + 1, total + nums[i])
        #backtracking step subset.pop

        res = []
        sub = []

        def dfs(i, total):
            #base case
            if i >= len(nums) or total > target:
                return
            elif total == target:
                print(sub)
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i, total + nums[i])
            sub.pop()
            dfs(i + 1, total)
        dfs(0, 0)
        return res