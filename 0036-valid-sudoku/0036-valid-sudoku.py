class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Initialize an array of 9 bitmasks for rows, columns, and 3x3 boxes
        rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.': 
                    continue
                
                # Represent the digit as a specific bit shift (e.g., '7' shifts 1 by 7 positions)
                mask = 1 << int(val)
                b = (r // 3) * 3 + (c // 3)
                
                # Fast bitwise check: if the bit is already set (1), a duplicate exists
                if (rows[r] & mask) or (cols[c] & mask) or (boxes[b] & mask):
                    return False
                
                # Bitwise OR sets the bit to 1, marking the number as seen
                rows[r] |= mask
                cols[c] |= mask
                boxes[b] |= mask
                
        return True

        