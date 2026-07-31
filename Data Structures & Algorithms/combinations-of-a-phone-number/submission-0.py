class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_char = {'2' : "abc", 
                    '3': "def", 
                    '4':"ghi", 
                    '5': "jkl", 
                    '6': "mno", 
                    '7': "pqrs", 
                    '8': "tuv", 
                    '9': "wxyz"}
        res = []
        def backtrack(index, current_combo):
        # base case: what condition means you've picked a letter for every digit?
            if index >= len(digits):
                res.append(current_combo)
                return
    
            letters = digit_to_char[digits[index]]
            for letter in letters:
                backtrack(index + 1, current_combo + letter)
        if digits:
            backtrack(0, "")
        return res
                

        # 1. make a choice (add letter to current path)
        # 2. recurse to the next index
        # 3. undo the choice (backtrack)