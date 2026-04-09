class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        p1 = 0
        p2 = m-1

        # 1, 10, 23 --- 3
        rowI = 0
        while True:
            if p1 >= p2-1:
                print("close check", p1, p2)
                num1 = matrix[p1][0]
                num2 = matrix[p2][0]
                if target < num1:
                    if p1 == 0:
                        return False
                    rowI = p1-1
                elif num1 < target < num2:
                    rowI = p1
                elif num2 < target:
                    rowI = p2
                else:
                    return True
                

                print("within row i#" + str(rowI))
                break

            pm = (p1+p2) // 2
            num = matrix[pm][0]

            if num < target:
                p1 = pm
            elif num > target:
                p2 = pm
            else: # target is 0th element in pm's array row
                return True
        
        row = matrix[rowI]
        p1 = 0
        p2 = n-1
        while True:
            print("2nd loop", p1, p2)
            if p1 >= p2-1:
                print("Final check")
                num1 = row[p1]
                num2 = row[p2]

                if target == num1 or target == num2:
                    return True
                else:
                    return False

            pm = (p1+p2) // 2
            num = row[pm]
            print(pm, num)

            if num < target:
                p1 = pm
            elif num > target:
                p2 = pm
            else:
                return True

            