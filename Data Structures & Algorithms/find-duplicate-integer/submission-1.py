class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 4-100 ^ 5-101 = 1-001 -> ^ 4-100 = 5-101
        # 1-001 ^ 3-011 = 2-010 -> ^ 5-101 = 7-111
        # 9-1001

        n = len(nums)
        for i, num in enumerate(nums):
            ic = abs(num)-1
            check = nums[ic]
            #print(i, num, ic, check)
            if check < 0:
                return ic+1
            nums[ic] *= -1
        
        return -1