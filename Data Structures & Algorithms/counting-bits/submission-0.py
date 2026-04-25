full = [0]

class Solution:
    def countBits(self, n: int) -> List[int]:
        l = len(bin(n))
        if len(full) > n:
            return full[:n+1]
        
        for i in range(len(full), n+1):
            full.append(bin(i).count('1'))
        
        return full