class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        keys = []
        most_freq_nums = [0] * k
        n = len(nums)
        bins = [0] * n

        for i, num in enumerate(nums):
            bins[i] = []
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
                keys.append(num)
        
        min_num_allowed = 99999
        index_of_mna = 0
        for i, key in enumerate(keys):
            bins[hashmap[key]-1].append(key)
        
        index_on = 0
        for i in range(n-1, -1, -1):
            for j in range(len(bins[i])):
                most_freq_nums[index_on] = bins[i][j]
                index_on += 1
                if index_on == k:
                    return most_freq_nums
        
        return []




