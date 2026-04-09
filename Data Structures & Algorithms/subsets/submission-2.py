class Solution:
    def backtrack(self, start, current):
        l = len(current) # Reminder: len(list) runs in O(1) time in python
        if l == self.k:
            self.ans.append(current[:])
            return
        
        #for i in range(start, self.n): # start may be larger than self.n, so sometimes this doesn't run, but this is intended
        for i in range(start, self.n-self.k+l+1):
            current.append(self.nums[i])
            self.backtrack(i+1, current)
            current.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = [[]]
        self.nums = nums
        self.n = n = len(nums)
        '''
        for i in range(1,self.n+1):
            self.k = i
            self.backtrack(0, [])
            '''
        # Another way:
        for i in range(n):
            cur = nums[i]
            cur = [cur]
            cur_len = len(self.ans)
            for j in range(cur_len):
                self.ans.append(self.ans[j] + cur)
        
        return self.ans

        