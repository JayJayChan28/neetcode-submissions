class Solution:
    def isValid(self, s: str) -> bool:
        #intialize set to store all opening characters
        #hash_map structure to map clsing brackets to opening brackets
        #check top of stack to see if it maps to correct value and pop it
        # return stack --> if its empty return true and it isnt empty return false

        hash_map = {')':'(', '}':'{', ']':'['}
        set_checks = set(['(', '{', '['])
        stack = []
        for string in s:
            if string in set_checks:
                stack.append(string)
            elif string in hash_map:
                if not stack:
                    return False
                if hash_map[string] != stack.pop():
                    return False
        return not stack

