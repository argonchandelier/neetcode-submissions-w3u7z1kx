class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxL = 1
        n = len(s)

        p1 = 0
        p2 = 0
        char1 = s[p1]
        char2 = s[p2]
        charCounts = {} #{char1: 0}
        l = 1
        while True:
            if p2 >= n:
                l -= 1
                charn = char1
                print("\nDONE", charCounts, s[p1:p2+1], l)
                while True:
                    p1 -= 1
                    if p1 < 0:
                        break
                    char1 = s[p1]
                    charCounts[char1] += 1
                    l += 1
                    print(l, charCounts[charn], k)
                    if l > charCounts[charn] + k:
                        break
                    if l > maxL:
                        maxL = l
                return maxL
            
            #l = p2-p1+1

            char1 = s[p1]
            char2 = s[p2]

            if char2 not in charCounts:
                charCounts[char2] = 1
            else:
                charCounts[char2] += 1
            
            print("")
            print(charCounts, s[p1:p2+1])
            badL = l > charCounts[char1] + k
            if not badL:
                print("good", l, charCounts, s[p1:p2+1])
                if l > maxL:
                    maxL = l
                p2 += 1
                print(p1, p2, s[p1:p2+1])
                l += 1
            else:
                #charCounts[char2] -= 1
                #p2 -= 1
                #char2 = s[p2]
                x=0
            while badL:
                print("bad", charCounts, s[p1:p2+1])
                charCounts[char1] -= 1
                p1 += 1
                print(p1, p2, charCounts, s[p1:p2+1])
                l -= 1
                char1 = s[p1]
                badL = l > charCounts[char1] + k
                if not badL:
                    print("GOOD", l, charCounts, s[p1:p2+1])
                    if l > maxL:
                        maxL = l
                    p2 += 1
                    print(p1, p2, s[p1:p2+1])
                    l += 1



            '''
            badL = l > charCounts[char1] + k # charCounts[char1] should already be checked before 
            if badL:
                print("bad l")
                charCounts[char1] -= 1
                l -= 1
            else:
                if char2 in charCounts:
                    charCounts[char2] += 1
                else:
                    charCounts[char2] = 1
                l += 1

            print("\np1, p2", p1, p2, "length l:", l)
            #print("chars 1&2", charCounts[char1], charCounts[char2])
            print("charCounts[char1], k, l:", charCounts[char1], k, l, s[p1:p2+1])
            #print("chars 1&2", char1, char2, charCounts.get(char1, "0"), charCounts.get(char2, "0"))
            print("charCounts:", charCounts)

            

            if badL:
                
                p1 += 1
                #charCounts[char1] -= 1


                #char1 = s[p1]

                #charCounts[char2] -= 1
                #p2 -= 1
                
                #char2 = s[p2]
            else:

                if l > maxL:
                    print("new max l:", l)
                    maxL = l
                p2 += 1
                #char2 = s[p2]
            
            
            #print(s[p1:p2+1])
            '''
        


        