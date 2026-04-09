class Solution:
    def isPalindrome(self, s):
        p1=0
        p2=len(s)-1
        while p1 < p2:
            c1 = s[p1]
            c2 = s[p2]
            if c1 != c2:
                return False
            p1 += 1
            p2 -= 1

        return True

    '''
    def backtrack(self, s):
        if s == "":
            return
        if self.isPalindrome(s):
            self.ans.append(s)
        
        for j in range(len(s)):
            newS = s[:j] + s[j+1:]
            self.backtrack(newS)
    '''
    def backtrack(self, i, s): #, partition, k): # i is the starting index of s in the original self.s; k is kth value in partition
        sl = len(s)
        #if sl == 1:
        #    return [s]

        fullRes = []
        if self.isPalindrome(s):
            fullRes = [[s]]
        for j in range(1, sl):
            s1 = s[:j]
            s2 = s[j:]
            print("s1 and s2:", s1, s2)
            #palin1 = self.isPalindrome(s1)
            #palin2 = self.isPalindrome(s2)
            #newPartit = partition.copy()
            #newPartit.pop(k)
            #newPartit.insert(k, s2)
            #newPartit.insert(k, s1)
            #if palin1 and palin2:
            #    fullRes += [s1, s2]

            # results will be all substring sets that are palindromes
            resL = self.backtrack(i, s1)#, newPartit, k)
            #resR = self.backtrack(i+j, s2)#, newPartit, k+1)
            resR = [[s2]] if self.isPalindrome(s2) else []

            #NO-  fullRes += resL + resR
            # We need every combo of l and r
            print("resl, resr", resL, resR)
            if resL and resR:
                for resl in resL:
                    for resr in resR:
                        print("adding to fullres:", resl+resr)
                        fullRes.append(resl + resr)
            print("current fullres:", fullRes)
        print(fullRes)
        return fullRes

    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.s = s

        res = self.backtrack(0, s)#, [s])
        print("final:", res)
        return res

        print(self.ans)
        return self.ans
        