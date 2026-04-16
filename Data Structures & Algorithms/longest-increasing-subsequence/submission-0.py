class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[nums[0], 1]]
        for i, num in enumerate(nums[1:], start = 1):
            curCount = 1
            for j, (end, count) in enumerate(dp):
                if end < num:
                    curCount = max(curCount, count+1)
                    continue
                elif end > num:
                    dp.append([num, curCount])
                    dp.sort()
                    break
                dp[j][1] = max(curCount, count)
                break
            else:
                dp.append([num, curCount])
        
        return max(elem[1] for elem in dp)




