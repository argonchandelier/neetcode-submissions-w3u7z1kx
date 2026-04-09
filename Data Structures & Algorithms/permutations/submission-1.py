class Solution:
    def backtrack(self, remaining, new):
        left = len(remaining)
        if left == 0:
            self.ans.append(new)
            return
        
        for i in range(left):
            #num = remaining[i]
            #nextRem = remaining[:i] + remaining[i+1:]
            nextRem = remaining.copy()
            num = nextRem.pop(i)
            self.backtrack(nextRem, new + [num])

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []

        self.backtrack(nums, [])

        return self.ans
        