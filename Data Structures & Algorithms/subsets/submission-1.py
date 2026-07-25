class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, subset):
            #base case when out of range
            if i == len(nums):
                res.append(subset.copy())
                return
            #decission tree, add
            subset.append(nums[i])
            dfs(i + 1, subset)

            #backtracking step
            subset.pop()

            #dont add new value but still incredment 
            dfs(i + 1, subset)
        
        dfs(0, subset)
        return res

            
