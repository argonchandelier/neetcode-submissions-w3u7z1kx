class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        s1map = {}
        for char in s1:
            s1map[char] = s1map.get(char, 0) + 1
        print(s1map)

        p1 = 0
        p2 = m-1

        # O((n-m)*m) = O(n*m - m^2) => converges to n for n >> m (kinda n*m but m~=k, O(k)=O("1") for large diff), if n ~= m, converges to O(1)
        while True:
            if p2 >= n:
                return False
            s2map = {}
            for char in s2[p1:p2+1]:
                s2map[char] = s2map.get(char,0)+1
            if s1map == s2map:
                return True
            
            p1+=1
            p2+=1
