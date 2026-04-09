import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for pt in points:
            x, y = pt
            dist = (x**2 + y**2)**(0.5)
            heapq.heappush(heap, (dist, pt))
        
        ans = []
        for i in range(k):
            vals = heapq.heappop(heap)
            dist, pt = vals
            ans.append(pt)
        
        return ans