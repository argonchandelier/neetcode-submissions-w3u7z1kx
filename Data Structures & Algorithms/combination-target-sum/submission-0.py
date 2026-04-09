class Solution:
    def backtrack(self, l, s, start):
        if s == self.target:
            self.ans.append(l)
            return
        if s + self.minim > self.target:
            return
        #print(i, l, s)
        
        for j in range(start, self.n):
            num = self.nums[j]
            self.backtrack(l + [num], s+num, j)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.n = len(nums)
        self.nums = nums
        self.target = target
        self.minim = min(nums)
        self.ans = []

        self.backtrack([], 0, 0)

        return self.ans
        