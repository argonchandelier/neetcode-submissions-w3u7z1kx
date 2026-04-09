class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = ""
        last_closing = True
        for i in range(n):
            char = s[i]
            if char == "(":
                stack += ")"
            elif char == "{":
                stack += "}"
            elif char == "[":
                stack += "]"
            elif char == ")" or char == "}" or char == "]":
                if len(stack) == 0:
                    return False
                last = stack[-1]
                if last != char:
                    return False
                stack = stack[:-1]
        if len(stack) > 0:
            return False
        return True



