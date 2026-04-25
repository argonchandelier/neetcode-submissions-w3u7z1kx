class Solution:
    def reverseBits(self, n: int) -> int:
        s = ['0']*32
        i = 0
        while n > 0:
            s[i] = str(n & 1)
            n = n >> 1
            i += 1
        
        return int(''.join(s), 2)