class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hash_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def dfs(sub, i):
            if i >= len(digits):
                res.append("".join(sub))
                return
            for j in range(len(hash_map[digits[i]])):
                digit = digits[i]
                print(hash_map[digit][j])
                sub.append(hash_map[digit][j])
                dfs(sub, i + 1)
                sub.pop()
        dfs([], 0)
        if digits == "":
                res = []
        return res