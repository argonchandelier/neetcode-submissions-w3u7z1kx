class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {num: i for i, num in enumerate(nums)}
        print(hashmap)
        n = len(nums)
        ans_sets = []
        ans = []

        for i, num1 in enumerate(nums):
            if i > n-3:
                break
            #for j, num2 in enumerate(nums[(i+1):]):
            for j in range(i+1, n):
                num2 = nums[j]
                s=num1+num2
                if (-s) in hashmap:
                    k = hashmap[-s]
                    if k > i and k > j:
                        triplet = [num1, num2, -s]
                        triplet_set = set(triplet)
                        if triplet_set not in ans_sets:
                            print(i, j, k)
                            ans_sets.append(triplet_set)
                            ans.append(triplet)
        
        return ans
