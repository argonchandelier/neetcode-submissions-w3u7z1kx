class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n // 2):
            for c in range((n+1)// 2):
                nr, nc = n-r-1, n-c-1
                matrix[r][c], matrix[nc][r], matrix[n-r-1][nc], matrix[c][nr] = \
                matrix[nc][r], matrix[nr][nc], matrix[c][nr], matrix[r][c]
