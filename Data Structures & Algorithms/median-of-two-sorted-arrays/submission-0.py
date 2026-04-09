class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        t = m+n
        half = t//2
        half2 = (t+1)//2

        # a <= b
        if n < m:
            numsA = nums2.copy()
            numsB = nums1.copy()
            a = n
            b = m
        else:
            numsA = nums1.copy()
            numsB = nums2.copy()
            a = m
            b = n
        
        print("nums A&B:", numsA, numsB)
        
        #pA = (a-1) // 2 # 5->2; 8->3; index of last in partition
        #pB = -(half2-(pA+1)) # half: 6.5->6, but 7 must remain, so pA=2 means we have 3, so we have 7-3=4 in B

        l = -1
        r = a-1
        while True:
            print("")
            pA = (l+r+1) // 2 # 5->2; 8->4; index of last in partition; takes bigger half
            #pB = b-(half2-(pA+1)) # t:10->half2:5 A3/B7->
            # b-half2+pA+1
            pB = half2-pA-1
            pA2 = pA+1
            pB2 = pB-1
            print("pA:", pA, "pB:", pB, "pA2:", pA2, "pB2:", pB2, "l:", l, "r:", r)
            
            '''
            if l == r:
                if t % 2 == 0:
                    return num1
                else:
                    return float(num1+num2)/2.0
            '''
            num1 = None
            num2 = None
            num3 = None
            num4 = None
            if pA > -1:
                num1 = numsA[pA] # right side of Al
            if 0 <= pB <= b-1:
                num2 = numsB[pB] # left side of Br
            if pA2 < a:
                num3 = numsA[pA2] # left side of Ar
            if 0 <= pB2 <= b-1:
                num4 = numsB[pB2] # right side of Bl
            print("num1:", num1, "num2:", num2, "nums3:", num3, "nums4:", num4)

            # Al<->Br
            '''
            if pA > -1: # pA exists; the left partition of A exists
                if 0 <= pB <= b-1: # right partition of B also exists
                    num1 = numsA[pA] # right side of Al
                    num2 = numsB[pB] # left side of Br
                    print("num1:", num1, "num2:", num2)
                    '''
            if num1 != None and num2 != None:
                if num1 > num2:
                    r = pA - 1
                    print("shifted r to", r)
                    continue

            # Bl<->Ar
            '''
            if pA < a-1: # pA2 exists; the right partition of A exists
                
                if 0 <= pB2 <= b-1: # left partition of B also exists
                    num3 = numsA[pA2] # left side of Ar
                    num4 = numsB[pB2] # right side of Bl
                    print("nums3:", nums3, "nums4:", nums4)
                    '''
            if num3 != None and num4 != None:
                if num4 > num3:
                    l = pA
                    print("shifted l to", l)
                    continue
            break
        # 1,2,3;1,2,3;;4,5;4,5,6,7,8 -> median is min of 2 left sides of Ar,Br
        # 1,2,3,4,5,6;_;;7,8;9,10,11,12,13
        # 1,2,3,4,5;6;;_;7,8,9,10,11,12,13
        # if t is even, then median is:
        # average of: max of 2 right sides of Al,Bl and min of 2 left sides of Ar,Br
        
        # XXXXXXXXAl+Bl <= Ar+Br ...or other way around...
        # Al+Bl >= Ar+Br
        # ^ is == iff t is even
        print("\n\nfinal pA, pB:", pA, pB, "pA2, pB2:", pA2, pB2)

        if num1 == None:
            medL = num4
        elif num4 == None:
            medL = num1
        else:
            medL = max(num1, num4)

        if t % 2 == 0:
            if num2 == None:
                if num3 == None:
                    print("very edge case?")
                    return medL
                medR = num3
            elif num3 == None:
                medR = num2
            else:
                medR = min(num2, num3)
            
            med = float(medL+medR) / 2.0
            print("Even med avg from", medL, medR, "is:", med)
            return med
        else:
            print("Odd med is just medL:", medL)
            return medL
        
        '''
        if num2 == None:
            medR = num3
        elif num3 == None:
            medR = num2
        else:
            medR = min(num2, num3)

        if t % 2 == 0: # even
            if num1 == None:
                if num4 == None:
                    print("very edge case?")
                    return medR
                medL = num4
            elif num4 == None:
                medL = num1
            else:
                medL = max(num1, num4)
            
            med = float(medL+medR) / 2.0
            print("Even med avg from", medL, medR, "is:", med)
            return med
        else: # odd
            print("Odd med is just medR:", medR)
            return medR
        '''

        '''
            if num1 > num2:
                r = pA - 1
            elif num1 < num2:
                l = pA
            else: # equal
                return num1
        '''

        '''
        #minimum = min(nums1[0], nums2[0])
        #maximum = max(nums1[-1], nums2[-1])
        
        # a <= b
        if n < m:
            numsA = nums2.copy()
            numsB = nums1.copy()
            a = n
            b = m
        else:
            numsA = nums1.copy()
            numsB = nums2.copy()
            a = m
            b = n
        
        # final pMid will be between (median of b) and (a+b-median of b)
        pMidA = (a-1) // 2 # if even, will be smaller of mids
        pMidB = (b-1) // 2

        pA = (a-1) // 2 # 5->2; 8->3; index of last in partition
        pB = t-(pA+1)
        
        while True:
            # 1,8,9,20,30; 2,6,16,26,36; 16>9 -> 1,2,6,8,9,16,20,26,30,36
            # 9,20,30; 2,6,16; 20>6
            # 9; 16
            #
            # 1,2,3,4,5; 6,7,8,9,10; 3<8
            # 3,4,5; 6,7,8
            #
            # 10,20,30,40,50; 11,12,13,39,45; 30>13
            # 10,20,30; 13,39,45; 20<39
            # 20,30; 13,39
        '''


