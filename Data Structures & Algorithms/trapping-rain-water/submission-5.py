class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        local_maxima = []
        
        # Forwards/Backwards Heighest Heights
        fhh = [0] * n
        bhh = [0] * n
        fhh[0] = height[0]
        bhh[-1] = height[-1]

        # Left/Right sums
        lSum = [0] * n
        rSum = [0] * n
        lSum[0] = height[0]
        rSum[-1] = height[-1]

        for i in range(1, n):
            h = height[i]
            bh = height[-1-i]

            lSum[i] = h + lSum[i-1]
            rSum[-1-i] += bh + rSum[-i]

            if fhh[i-1] < h:
                fhh[i] = h
            else:
                fhh[i] = fhh[i-1]
            if bhh[-i] < bh:
                bhh[-1-i] = bh
            else:
                bhh[-1-i] = bhh[-i]
        print(fhh, bhh)
        print(lSum, rSum)
        
        for i in range(n):
            h = height[i]

            prev_h = 0
            next_h = 0
            if i > 0:
                prev_h = height[i-1]
            if i < n-1:
                next_h = height[i+1]
            
            # the 'not' part disregards a local max that has a taller max on both sides
            if h >= prev_h and h >= next_h and not (fhh[i] > h and bhh[i] > h):
                local_maxima.append(i)
        
        if len(local_maxima) <= 1:
            return 0

        totalWaterArea = 0
        for i in range(len(local_maxima)-1):
            lm1i = local_maxima[i]
            lm2i = local_maxima[i+1]
            lm1h = height[lm1i]
            lm2h = height[lm2i]

            basinH = min(lm1h, lm2h)
            #basinL = lm2i-lm1i-1
            basinL = 0
            landArea = -1
            if basinH == lm1h: # min height is left side (or both)
                print("a", lm1i, lm2i, lm1h, lm2h)
                j = lm1i+1
                while True:
                    print("b", j)
                    h = height[j]
                    if h >= lm1h:
                        landArea = lSum[j-1] - lSum[lm1i]
                        break
                    basinL += 1
                    j += 1
            else:
                print("q", lm1i, lm2i, lm1h, lm2h)
                j = lm2i-1
                while True:
                    print("r", j)
                    h = height[j]
                    if h >= lm2h:
                        landArea = rSum[j+1] - rSum[lm2i]
                        break
                    basinL += 1
                    j -= 1

            #landArea = lSum[lm2i-1] - lSum[lm1i]
            
            fullArea = basinH*basinL
            waterArea = fullArea - landArea
            print("areas:", landArea, fullArea, waterArea)
            print(lm1i, lm2i, lm1h, lm2h)

            totalWaterArea += waterArea
        
        return totalWaterArea
