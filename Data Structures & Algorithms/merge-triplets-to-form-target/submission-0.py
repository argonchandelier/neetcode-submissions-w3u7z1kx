class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        check = [False, False, False]
        checkSum = 0
        for triplet in triplets:
            good = False
            for j, num in enumerate(triplet):
                if num > target[j]:
                    break
            else:
                for j, num in enumerate(triplet):
                    if check[j] or num != target[j]:
                        continue
                    check[j] = True
                    if sum(check) == 3:
                        return True

        return False