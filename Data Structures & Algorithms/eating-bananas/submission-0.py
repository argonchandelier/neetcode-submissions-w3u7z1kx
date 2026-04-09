class Solution:
    def isKTooSmall(self, k):
        h_full = 0
        for i, pile in enumerate(self.piles):
            h_full += pile // k
            if pile % k > 0:
                h_full += 1
        
        return h_full > self.h
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # pile_i /(ceiling) k = h_i, sum(h_i) = h 
        # k * h_i = pile_i or more
        # 1 <= k <= m
        self.h = h
        self.n = n = len(piles)
        self.piles = piles

        kl = 1
        kr = max(piles)
        while True:
            if kl == kr:
                break

            kMid = (kl+kr) // 2
            isTooSmall = self.isKTooSmall(kMid)

            if isTooSmall:
                kl = kMid + 1
            else:
                kr = kMid
        
        return kl

