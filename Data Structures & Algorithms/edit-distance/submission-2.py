class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        seen = {}

        def dfs(i1, i2):
            if i1 == l1:
                return l2-i2
            if i2 == l2:
                return l1-i1
            save = (i1, i2)
            if save in seen:
                return seen[save]

            c1, c2 = word1[i1], word2[i2]
            if c1 == c2:
                res = dfs(i1+1, i2+1)
            else:
                res = 1 + min(dfs(i1, i2+1), dfs(i1+1, i2), dfs(i1+1, i2+1))

            seen[save] = res
            return res
        
        return dfs(0, 0)

