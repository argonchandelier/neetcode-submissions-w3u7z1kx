"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        times = []
        starts = set()
        for interv in intervals:
            s, e = interv.start, interv.end
            times.append(s)
            times.append(e)
            if s in starts:
                return False
            starts.add(s)
        times.sort()
        n = len(times)
        for interv in intervals:
            s, e = interv.start, interv.end
            l, r = 0, n-1
            while l <= r:
                c = (l+r)//2
                num = times[c]

                if num <= s:
                    l = c+1
                else:
                    r = c-1
            if l == n or times[l] != e:
                return False
        
        return True



