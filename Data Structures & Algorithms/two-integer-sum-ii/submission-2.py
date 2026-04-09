class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        p1 = 0
        p2 = n-1
        while True:
            n1 = numbers[p1]
            while True:
                n2 = numbers[p2]
                s = n1+n2
                if s < target:
                    break
                elif s == target:
                    return [p1+1, p2+1]
                else:
                    p2 -= 1
            p1 += 1
        
