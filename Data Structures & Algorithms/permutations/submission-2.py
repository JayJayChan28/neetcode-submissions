class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # base case i >= len(nums)
        res = []

        #untracked values
        tmp_list = [False] * len(nums)

        def dfs(i, path, tmp_lists):
            if i >= len(nums):
                res.append(path.copy())
                return 
            for j in range(len(nums)):
                if tmp_list[j]:
                    continue 
                tmp_list[j] = True
                path.append(nums[j])
                dfs(i + 1, path, tmp_list)
                path.pop()
                tmp_list[j] = False
        dfs(0, [], tmp_list)
        return res
