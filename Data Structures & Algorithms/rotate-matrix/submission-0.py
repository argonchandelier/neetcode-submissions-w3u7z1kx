class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n // 2):
            for c in range((n+1)// 2):
                matrix[r][c], matrix[n-c-1][r], matrix[n-r-1][n-c-1], matrix[c][n-r-1] = \
                matrix[n-c-1][r], matrix[n-r-1][n-c-1], matrix[c][n-r-1], matrix[r][c]
