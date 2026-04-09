class Solution:
    def hashify(self, l):
        h = {}
        for i, num in enumerate(l):
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        return h
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = [[]]
        #self.sets = []
        self.hashes = []
        self.n = n = len(nums)

        for i in range(n):
            cur_len = len(self.ans)
            num = nums[i]
            for j in range(cur_len):
                subset = self.ans[j]
                newSubset = subset + [num]
                #newSubsetSet = set(newSubset)
                newSubsetHash = self.hashify(newSubset)
                #if newSubsetSet not in self.sets:
                if newSubsetHash not in self.hashes:
                    self.ans.append(newSubset)
                    #self.sets.append(newSubsetSet)
                    self.hashes.append(newSubsetHash)
        
        return self.ans
