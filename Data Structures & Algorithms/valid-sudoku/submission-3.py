class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            seen = set() 
            for col in range(9):
                elem = board[row][col]
                if elem == ".":
                    continue
                if elem in seen:
                    return False
                seen.add(elem)
        
        for col in range(9):
            seen = set() 
            for row in range(9):
                elem = board[row][col]
                if elem == ".":
                    continue
                if elem in seen:
                    return False
                seen.add(elem)
        
        for square in range(9):
            seen = set()
            for dum_row in range(3):
                for dum_col in range(3):
                    row = (square // 3) * 3 + dum_row
                    col = (square % 3) * 3 + dum_col
                    elem = board[row][col]
                    if elem == ".":
                        continue
                    if elem in seen:
                        return False
                    seen.add(elem)
        
        return True
