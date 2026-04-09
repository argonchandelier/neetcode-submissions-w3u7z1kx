class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = n
        p1 = 0
        p2 = n-1
        while l > 2:
            midI = p1 + (l // 2)
            print(p1, p2, midI)
            midN = nums[midI]
            if midN < target:
                p1 = midI
            elif midN > target:
                p2 = midI
            else:
                return midI
            l = (p2-p1+1)
        
        if nums[p1] == target:
            return p1
        elif nums[p2] == target:
            return p2 
        return -1
