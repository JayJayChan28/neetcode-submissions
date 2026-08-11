class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #base case
        res = []
        sub = []
        marked_list = [False] * len(nums)

        #marked will store the list of visited values
        def dfs(sub, marked):
            #base case, we reach end of nums
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
            for j in range(len(nums)):
                #if the value is visited we skip
                if marked[j]:
                    continue
                
                sub.append(nums[j])
                marked[j] = True
                dfs(sub, marked)
                marked[j] = False
                sub.pop()
        dfs(sub, marked_list)
        return res
            