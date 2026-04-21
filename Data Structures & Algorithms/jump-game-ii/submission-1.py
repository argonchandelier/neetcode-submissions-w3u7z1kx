class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        # bfs
        prev, nxt = 1, nums[0]
        if nxt >= n-1:
            return 1
        for ans in range(2, 1000):
            mx = nxt+1
            for ind in range(prev, nxt+1):
                num = nums[ind]
                mx = max(mx, num + ind)
            if mx >= n-1:
                return ans
            prev, nxt = nxt+1, mx
