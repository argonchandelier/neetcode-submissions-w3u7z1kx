class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        c = 1
        for i, d in enumerate(digits[::-1]):
            c, d = divmod(d+c, 10)
            ans.append(d)
        else:
            if c == 1:
                ans.append(1)
        
        ans.reverse()
        return ans