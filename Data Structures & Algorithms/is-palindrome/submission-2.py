class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n-1
        while True:
            if i >= j:
                return True

            while True:
                charInt1 = ord(s[i])
                if 97 <= charInt1 <= 122 or 48 <= charInt1 <= 57:
                    break
                elif 65 <= charInt1 <= 90:
                    charInt1 += 32
                    break
                i += 1
                if i == n:
                    return True
            while True:
                charInt2 = ord(s[j])
                if 97 <= charInt2 <= 122 or 48 <= charInt1 <= 57:
                    break
                elif 65 <= charInt2 <= 90:
                    charInt2 += 32
                    break
                j -= 1
            
            if charInt1 != charInt2:
                return False
            i += 1
            j -= 1