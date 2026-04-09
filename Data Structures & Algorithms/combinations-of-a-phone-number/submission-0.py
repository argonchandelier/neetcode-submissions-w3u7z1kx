class Solution:
    def backtrack(self, depth, s):
        if depth == self.n:
            self.ans.append(s)
            return
        
        digit = self.digits[depth]
        possibilities = self.m[digit]
        for poss in possibilities:
            self.backtrack(depth+1, s+poss)

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        self.m = {"2": ["a", "b", "c"], 
        "3": ["d", "e", "f"], 
        "4": ["g", "h", "i"], 
        "5": ["j", "k", "l"], 
        "6": ["m", "n", "o"], 
        "7": ["p", "q", "r", "s"], 
        "8": ["t", "u", "v"], 
        "9": ["w", "x", "y", "z"], }
        self.n = len(digits)
        self.digits = digits
        self.ans = []

        self.backtrack(0, "")

        return self.ans
        