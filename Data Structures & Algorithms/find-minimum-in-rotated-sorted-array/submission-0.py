class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        p1 = 0
        p2 = n-1

        while True:
            if p1 == p2:
                return nums[p1]

            pMid = (p1+p2)//2 # might be the same as p1, but wont be p2

            num1 = nums[p1]
            num2 = nums[p2]
            numMid = nums[pMid]

            if numMid > num2:
                p1 = pMid + 1
            else:
                p2 = pMid ###

