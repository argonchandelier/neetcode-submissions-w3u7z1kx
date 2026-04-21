"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n == 0:
            return 0
        intervs = []
        for interv in intervals:
            intervs.append([interv.start, interv.end])
        intervs.sort()

        heap = [intervs[0][1]]
        mx = 1
        for i, (s, e) in enumerate(intervs[1:], start=1):
            while heap and s >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
            mx = max(mx, len(heap))

        return mx




