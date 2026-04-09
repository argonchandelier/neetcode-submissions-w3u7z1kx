import heapq
from collections import deque
INF = float('inf')

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #return self.crazyCompute(tasks, n)
        np = n+1
        valsMap = {}
        for task in tasks:
            if task in valsMap:
                valsMap[task] -= 1
                continue
            valsMap[task] = -1

        #vals = sorted(valsMap.values())
        heap = list(valsMap.values())
        heapq.heapify(heap)
        cooldown = deque()

        time = 0
        while heap or cooldown:
            time += 1
            while cooldown and cooldown[1] == time:
                val = cooldown.popleft()
                cooldown.popleft()
                heapq.heappush(heap, val)
            #print(f"{time = }, {heap = }, {cooldown = }")
            if not heap:
                continue
            mx = heapq.heappop(heap)
            mx += 1
            if mx < 0:
                cooldown.append(mx)
                cooldown.append(time + np)
        
        return time

    
    def crazyCompute(self, tasks, n):
        np = n+1
        valsMap = {}
        for task in tasks:
            if task in valsMap:
                valsMap[task] += 1
                continue
            valsMap[task] = 1

        vals = sorted(valsMap.values())

        ans = self.solve(vals, np)
        return ans

    def naiveSolve(self, vals, np):
        vals.sort(reverse=True)
        size = len(vals)
        c = 0
        while vals[0] > 0:
            if size <= np:
                # give extra n*max(vals) (vals left anyway)
                finalAdd = vals.count(max(vals))
                secondAdd = np * (max(vals) - 1)  # plus num values equal to max value # ...old: (len(vals) minus number of num0s_in_vals) -> num_non0s_in_vals
                firstAdd = c * np
                return firstAdd + secondAdd + finalAdd
            for i in range(np):
                vals[i] -= 1
                if vals[i] == 0:
                    size -= 1
            
            vals.sort(reverse=True)  # Uses timsort: very efficient since vals almost already sorted
            c += 1

    def solve(self, vals, np):
        # args: vals and np (from task list and n0+1)
        nTasks = sum(vals) # or len of task list
        
        l=len(vals)
        if np >= l:
            ans = (max(vals)-1)*np + vals.count(max(vals))
            return ans
        
        # Efficient, but only uncomment once testing finished
        if nTasks <= l:
            return self.naiveSolve(vals, np)
            
        h = []
        w = []
        h.append(vals[0])
        ilast = 0
        for i, n in enumerate(vals[1:], start=1):
            if n > h[-1]:
                w.append(i-ilast)
                h.append(n)
                ilast = i
        w.append(l-ilast)
        backCount = 0
        curWi1=-1
        for wi in range(len(w)-1,-1,-1):
            width = w[wi]
            backCount += width
            if backCount >= np:
                #ib = w
                curWi1 = wi
                break
        curWi2 = curWi1#+1
        ia = l-backCount
        ib = ia + w[curWi1]
        ic = ib + w[curWi1+1] if curWi1+1 < len(w) else l
        
        m2 = h[curWi1]
        m3 = h[curWi1+1] if curWi1+1 < len(w) else INF
        m1 = m3-m2
        m4 = h[curWi1-1] if curWi1 > 0 else 0
        m5 = m2-m4
        
        n1 = w[curWi1+1] if curWi1+1 < len(w) else 0 #ic-ib
        n2 = w[curWi1] #ib-ia
        n4 = w[curWi1-1] if ia > 0 else 0
        sp = np+n2-(l-ia) #np+n2-l
        T = 0
        
        C = 0
        for _ in range(100):
            cr = (m1*n2+T-sp) // (n2-sp) if ib < ic and sp < n2 else INF
            cf = (m2*n2-T) // sp
            cl = (n2*(m5-1)-T+sp-1) // sp if ia > 0 else cf
            c = min(cl, cr)
            C += c
            
            spct = sp*c+T
            if c == cf and ia == 0:
                finalAdd1 = (max(vals)-C-1)*np
                finalAdd2 = w[-1]
                T = spct % n2
                if ib == l:
                    finalAdd2 = n2-T if T > 0 else 0
                    finalAdd1 = 0
                elif ic == l and finalAdd1 == 0:
                    finalAdd1 = n2-T if T > 0 else 0
                nTasks = C*np
                nTasks += finalAdd1+finalAdd2
                return nTasks
            if cr < cl or (cl == cr and spct > n2*(m5-1)):
                T = spct % n2
                n2 += n1
                sp += n1
                ib = ic
                curWi2 += 1
                m2 = m3-c
                m3 = h[curWi2+1] - C if curWi2+1 < len(w) else INF
                m1 = m3-m2
                ic = ic+w[curWi2+1] if ic < l else l
                n1 = w[curWi2+1] if ib < ic else 0
            if cl <= cr:
                T = (spct % n2) + n4
                ia -= n4
                curWi1 -= 1
                n2 += n4
                n4 = w[curWi1-1] if curWi1 > 0 else 0
                m3 -= c
                m2 = m4+1
                m1 = m3-m2
                m4 = h[curWi1-1] if curWi1 > 0 else 0
                m5 = m2-m4
        
        return -2
            
        