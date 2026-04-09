class Solution:
    def backtrack(self, start, current):
        if len(current) == self.k:
            self.ans.append(current[:])
            return
        
        for i in range(start, self.n):
            current.append(self.nums[i])
            self.backtrack(i+1, current)
            current.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = [[]]
        self.nums = nums
        self.n = len(nums)
        for i in range(1,self.n+1):
            self.k = i
            self.backtrack(0, [])
        
        return self.ans

        