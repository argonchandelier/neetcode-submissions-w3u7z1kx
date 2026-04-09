import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        print(f"{heap = }")

        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            diff = y-x
            if diff < 0:
                heapq.heappush(heap, diff)

        return -heap[0] if heap else 0
        