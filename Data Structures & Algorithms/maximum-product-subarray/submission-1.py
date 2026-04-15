class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        poss = [0]*(n+1)
        negs = [0]*(n+1)

        for i, num in enumerate(nums, start=1):
            lastPos, lastNeg = poss[i-1], negs[i-1]
            if num > 0:
                poss[i] = lastPos*num if lastPos != 0 else num
                negs[i] = lastNeg*num
            elif num < 0:
                poss[i] = lastNeg*num
                negs[i] = lastPos*num if lastPos != 0 else num

        mx = max(poss)
        return mx if mx > 0 else max(negs[1:])

