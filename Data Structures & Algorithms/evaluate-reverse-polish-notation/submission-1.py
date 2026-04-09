class Solution:
    def add(self, a, b):
        return a+b
    def subtract(self, a, b):
        return a-b
    def mult(self, a, b):
        return a*b
    def divide(self, a, b):
        return int(a/b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": self.add, "-": self.subtract, "*": self.mult, "/": self.divide}
        n = len(tokens)

        for i in range(n):
            token = tokens[i]
            if token in operators:
                op2 = int(stack[-1])
                stack.pop()
                op1 = int(stack[-1])
                stack.pop()

                result = operators[token](op1, op2)
                stack.append(result)
                print(stack, op1, op2, token)
            else:
                stack.append(int(token))
        
        return int(stack[-1])