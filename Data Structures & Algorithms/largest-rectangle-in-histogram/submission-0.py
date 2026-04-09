class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        min_stack_for = [0]
        min_stack_back = [n-1]
        lengths_for = [-1] * n
        lengths_back = [-1] * n
        lengths = [-1]*n
        areas = [-1]*n

        for i in range(1, n):
            h = heights[i]
            while min_stack_for:
                lastI = min_stack_for[-1]
                lastH = heights[lastI]
                if h < lastH:
                    lengths_for[lastI] = i - lastI - 1
                    min_stack_for.pop()
                else:
                    break
            min_stack_for.append(i)
        for i in range(len(min_stack_for)):
            index = min_stack_for[i]
            lengths_for[index] = n-index-1

        for i in range(n-2, -1, -1):
            h = heights[i]
            while min_stack_back:
                lastI = min_stack_back[-1]
                lastH = heights[lastI]
                #print("lastI/H, i,h:", lastI, lastH, i, h, heights[5])
                if h < lastH:
                    #print("lengths back popped:", lastI, i, lastI-i-1)
                    lengths_back[lastI] = lastI - i - 1
                    min_stack_back.pop()
                else:
                    break
            min_stack_back.append(i)
        for i in range(len(min_stack_back)):
            index = min_stack_back[i]
            lengths_back[index] = index
        
        print(lengths_for, "---", lengths_back)

        for i in range(n):
            l = lengths[i] = lengths_for[i] + lengths_back[i] + 1
            areas[i] = l*heights[i]
        
        print(lengths)
        print(areas)
        ans = max(areas)

        return ans
        