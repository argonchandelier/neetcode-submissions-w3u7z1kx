from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cur = {0: 1}
        for num in nums:
            nxt = defaultdict(int)
            for csum, amount in cur.items():
                nxt[csum + num] += amount
                nxt[csum - num] += amount
            cur = nxt
        
        return cur[target]
