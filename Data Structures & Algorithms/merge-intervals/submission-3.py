class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print(f"{intervals = }")
        n = len(intervals)
        i = 0
        merges = []
        while i < n:
            s, e = intervals[i]
            jf, maxe = n-1, e
            for j in range(i+1, n):
                if maxe < intervals[j][0]:
                    jf = j-1
                    break
                maxe = max(maxe, intervals[j][1])
            if jf <= i:
                i += 1
                continue
            
            merges.append([i, jf, s, maxe])
            i = jf+1
        
        offset = 0
        for i, jf, s, e in merges:
            intervals[i-offset:jf+1-offset] = [[s, e]]
            offset = n - len(intervals)
        
        return intervals
            
                
