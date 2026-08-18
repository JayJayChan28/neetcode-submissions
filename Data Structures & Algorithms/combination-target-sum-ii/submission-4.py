class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #1) sort --> sort the values asecending
        #2) skip where candidates[i] == candiates[i + 1]
        #3) contraint sum == target & base case i >= len(candidates)
        res = []
        candidates.sort()
        print(candidates)

        def dfs(sub, i, total):
            if total == target:
                res.append(sub.copy())
                return
            if i >= len(candidates) or total > target:
                return 
            sub.append(candidates[i])
            dfs(sub, i + 1, total + candidates[i])
            sub.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(sub, i + 1, total)
        dfs([], 0, 0)
        return res