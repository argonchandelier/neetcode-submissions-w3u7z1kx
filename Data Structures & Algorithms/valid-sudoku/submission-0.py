class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        subboxes = [[0] * 9 for i in range(9)]
        rows = [[0] * 9 for i in range(9)]
        cols = [[0] * 9 for i in range(9)]

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                    
                subbox_i = (j//3)+3*(i//3)
                cellm1 = int(cell)-1

                if subboxes[subbox_i][cellm1] == 1:
                    return False
                if rows[i][cellm1] == 1:
                    return False
                if cols[j][cellm1] == 1:
                    return False
                
                subboxes[subbox_i][cellm1] = 1
                rows[i][cellm1] = 1
                cols[j][cellm1] = 1
        
        return True
        


