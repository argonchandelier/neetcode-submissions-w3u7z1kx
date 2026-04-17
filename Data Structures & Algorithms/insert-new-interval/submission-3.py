class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval
        n = len(intervals)
        phase = 0
        phaseMap = {0: ns, 1: ne, 2: -1}
        phaseVal = ns
        indexes = [[n, 0], [n, 0]]
        i = 0
        while i < n:
            start, end = intervals[i]
            if phaseVal < start:
                indexes[phase] = [i, 0]
            elif start <= phaseVal <= end:
                indexes[phase] = [i, 1]
            else:
                i += 1
                continue
            phase += 1
            if phase == 2:
                break
            phaseVal = phaseMap[phase]
        
        i00, i01, i10, i11 = indexes[0][0], indexes[0][1], indexes[1][0], indexes[1][1]
        if i00 == i10:
            if i01 == i11 == 0:
                intervals.insert(i00, [ns, ne])
            elif i01 == 0 and i11 == 1:
                intervals[i00][0] = ns
            return intervals
        if i01 == 0:
            intervals[i00][0] = ns
        if i11 == 0:
            intervals[i10-1][1] = ne
        
        intervals[i00:i10 + i11] = [[intervals[i00][0], intervals[i10 - (i11 ^ 1)][1]]]
        return intervals
