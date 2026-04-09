class Solution:
    def backtrack(self, start, current):
        l = len(current)
        if l == self.k:
            #print(current[:])
            self.ans.append(current[:])
            return
        
        #for i in range(start, self.n): # start may be larger than self.n, so sometimes this doesn't run, but this is intended
        #print(start, self.n-l)
        for i in range(start, self.n-self.k+l+1):
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

        