class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #base case: when i >= len(canidiartes)
        #Contratsinos: no dub, use while candiates[i] != candiiates i + 1 as long
        #as cancdiies i + 1 is in range, then we increas i += 1
        candidates.sort()
        res = []

        def dfs(i, sub, total):
            if target == total:
                res.append(sub.copy())
                return
            if i >= len(candidates) or total > target:
                return
            sub.append(candidates[i])
            dfs(i + 1, sub, total + candidates[i])
            sub.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, sub, total)
        dfs(0, [], 0)
        return res