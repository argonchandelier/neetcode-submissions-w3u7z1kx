class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        c0 = 1
        r0 = 0 if 0 in matrix[0] else 1
        for r in range(m):
            if matrix[r][0] == 0:
                c0 = 0
                break

        for r, row in enumerate(matrix[1:], start=1):
            for c, num in enumerate(row[1:], start=1):
                if num == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r, row in enumerate(matrix[1:], start=1):
            if row[0] != 0:
                continue
            for c in range(1, n):
                matrix[r][c] = 0
        for c in range(1, n):
            if matrix[0][c] != 0:
                continue
            for r in range(m):
                matrix[r][c] = 0
        
        if r0 == 0:
            matrix[0] = [0]*n
        if c0 == 0:
            for r in range(m):
                matrix[r][0] = 0
        
        