class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        n = len(s)
        #if n == 0:
        #    return 0

        p1 = 0 # first char to read
        p2 = 0 # last char to read
        #lastChar = s[0]
        #hashmap = {"lastChar": lastChar, lastChar: 0}
        hashmap = {}
        while True:
            if p2 >= n:
                break
            #substr = s[p1:p2+1]
            lastChar = s[p2]

            if lastChar in hashmap and hashmap[lastChar] >= p1:
                lastI = hashmap[lastChar]
                #hashmap[lastChar] = p2
                p1 = lastI+1
                #p2 += 1
            else:
                l = p2-p1+1
                print("p1, p2:", p1, p2, "l:", l)
                if l > maxLength:
                    maxLength = l
            hashmap[lastChar] = p2
            p2 += 1
        
        return maxLength


        