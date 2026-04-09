class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        p1 = 0
        p2 = n-1

        while True:
            if p2 < p1:
                return -1

            pMid = (p1+p2) // 2

            num1 = nums[p1]
            num2 = nums[p2]
            numMid = nums[pMid]

            if num2 > num1: # contained is in order
                if target < numMid:
                    p2 = pMid - 1
                elif target > numMid:
                    p1 = pMid + 1
                else:
                    return pMid
            else: # contained not in order
                if num1 < target < numMid:
                    p2 = pMid - 1 # contained now in order
                elif num1 < numMid < target:
                    p1 = pMid + 1 # not in order
                elif target < numMid < num1:
                    p2 = pMid - 1 # not in order
                elif numMid < target < num1:
                    p1 = pMid + 1 # contained now in order
                elif target < num1 < numMid:
                    p1 = pMid + 1 # not in order
                elif numMid < num1 < target:
                    p2 = pMid - 1 # not in order
                elif target == num1:
                    return p1
                elif target == numMid:
                    return pMid
                elif target == num2:
                    return p2
                else: # down to last 2 nums but target already checked what's left
                    return -1
