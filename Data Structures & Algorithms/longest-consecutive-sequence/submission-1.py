class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {num: i for i, num in enumerate(nums)}
        print(hashmap)
        if hashmap == {}:
            return 0

        max_count = 1
        for i, num in enumerate(nums):
            if num-1 in hashmap:
                continue
            
            count = 1
            while True:
                num += 1
                if num not in hashmap:
                    break
                count += 1

            if count > max_count:
                max_count = count

        return max_count