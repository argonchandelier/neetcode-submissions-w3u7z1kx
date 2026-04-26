mp = {}
for i in range(10):
    mp[str(i)] = i
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        l1, l2 = len(num1), len(num2)
        ans = [0]*(l1+l2)
        for i, n1 in enumerate(num1[::-1]):
            n1 = mp[n1]
            for j, n2 in enumerate(num2[::-1]):
                n2 = mp[n2]
                ans[i+j] += n1*n2
        carry = 0
        for i, val in enumerate(ans):
            carry, dig = divmod(val+carry, 10)
            ans[i] = dig
        ans = [str(d) for d in ans[::-1]]
        ans = ''.join(ans)
        for i, c in enumerate(ans):
            if c != '0':
                return ans[i:]
