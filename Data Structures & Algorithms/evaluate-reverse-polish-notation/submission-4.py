class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+', '-', '*', '/'])
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] in operators:
                second_val = int(stack.pop())
                first_val = int(stack.pop())
                if tokens[i] == "+":
                    stack.append(first_val + second_val)
                if tokens[i] == "-":
                    stack.append(first_val - second_val)
                if tokens[i] == "*":
                    stack.append(first_val * second_val)
                if tokens[i] == "/":
                    stack.append(first_val / second_val)
                i += 1
            else: 
                stack.append(tokens[i])
                i += 1
        return int(stack[-1])
            