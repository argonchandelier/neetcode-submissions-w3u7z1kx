class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)
        x = s.count('1')

        return x