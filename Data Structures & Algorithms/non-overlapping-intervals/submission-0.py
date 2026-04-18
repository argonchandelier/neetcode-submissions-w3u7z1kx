class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)

        prevEnd = intervals[0][1]
        skips = 0
        for i, (s, e) in enumerate(intervals[1:], start=1):
            if s >= prevEnd:
                prevEnd = e
                continue
            prevEnd = min(prevEnd, e)
            skips += 1
        
        return skips