class Solution:
    def backtrack(self, l, s, start):
        if s == self.target:
            sl = set(l)
            if sl not in self.sets:
                self.ans.append(l)
                self.sets.append(sl)
            return
        if s + self.minim > self.target or start >= self.n: # First condition saves up to O(n) time
            return
        
        seen = {}
        for j in range(start, self.n):
            num = self.nums[j]
            if num in seen:
                continue
            self.backtrack(l + [num], s+num, j+1)
            seen[num] = j

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.nums = candidates
        self.target = target
        self.n = len(candidates)
        self.minim = min(candidates)
        self.ans = []
        self.sets = []

        self.backtrack([], 0, 0)

        return self.ans
        