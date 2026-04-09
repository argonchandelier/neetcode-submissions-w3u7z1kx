class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        step = [["(", 1, n-1]]
        for i in range(2*n-1):
            new_step = []
            for j in range(len(step)):
                part = step[j]
                string = part[0] # ans part
                depth = part[1] # how many more open than closed
                open_left = part[2] # open left

                if open_left == 0:
                    new_step.append([(string+")"), depth-1, 0])
                elif depth == 0:
                    new_step.append([(string+"("), 1, open_left-1])
                else:
                    new_step.append([(string+"("), depth+1, open_left-1])
                    new_step.append([(string+")"), depth-1, open_left])
            step = new_step
        
        l = len(step)
        output = [""] * l
        for i in range(l):
            output[i] = step[i][0]
        
        return output



