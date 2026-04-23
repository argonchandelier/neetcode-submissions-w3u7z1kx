class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}
        for c in s:
            if c in counts:
                counts[c] += 1
                continue
            counts[c] = 1
        
        ans = []
        chars, zeros, count = set(), 0, 0
        for c in s:
            count += 1
            chars.add(c)
            counts[c] -= 1
            if counts[c] == 0:
                zeros += 1
                if zeros == len(chars):
                    ans.append(count)
                    count = 0
        
        return ans

