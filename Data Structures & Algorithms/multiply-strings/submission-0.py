mp = {}
for i in range(10):
    mp[str(i)] = i
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        toadd = []
        ten = 1
        l1, l2 = len(num1), len(num2)
        for i, n1 in enumerate(num1[::-1]):
            n1 = mp[n1]
            num = 0
            carry = 0
            for j, n2 in enumerate(num2[:0:-1]):
                n2 = mp[n2]
                carry, digit = divmod(n1*n2 + carry, 10)
                num += digit*10**j
            num += (n1*mp[num2[0]] + carry) * 10**(l2-1)
            toadd.append(num*10**i)
        
        ans = str(sum(toadd))
        return ans
