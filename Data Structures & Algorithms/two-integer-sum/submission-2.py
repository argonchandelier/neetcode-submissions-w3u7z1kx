class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[str(nums[i])] = i
        for i in range(len(nums)):
            if str(target-nums[i]) in hashmap and i != hashmap[str(target-nums[i])]:
                return sorted([i, hashmap[str(target-nums[i])]])