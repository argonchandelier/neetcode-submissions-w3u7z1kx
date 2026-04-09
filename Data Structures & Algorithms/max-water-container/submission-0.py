class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        p1 = 0
        p2 = n-1
        maxArea = 0
        while True:
            num1 = heights[p1]
            num2 = heights[p2]

            num1Bigger = num1 > num2
            Min = min(num1, num2)
            dist = p2 - p1

            area = Min * dist
            if area > maxArea:
                maxArea = area
            
            if num1Bigger:
                p2 -= 1
            else:
                p1 += 1
            
            if p1 >= p2:
                break
        
        return maxArea

