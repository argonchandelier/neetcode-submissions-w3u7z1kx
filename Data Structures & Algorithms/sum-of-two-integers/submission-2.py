class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0b111111111111
        mx = mask >> 1

        while b:
            carry = (a&b) << 1
            a = (a^b) & mask
            b = carry & mask
        
        return a if a <= mx else ~(a^mask)
