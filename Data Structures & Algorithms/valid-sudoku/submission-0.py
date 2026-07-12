class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or len(board) != 9:
            return False
        seen = set()
        n = len(board)
        for i in range(n):
            seen.clear()
            for j in range(n):
                num = board[i][j]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)

        for j in range(n):
            seen.clear()
            for i in range(n):
                num = board[i][j]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)
        for x in (0, 3, 6):
            for y in (0, 3, 6):
                seen.clear()
                for i in range(3):
                    for j in range(3):
                        ii = x + i
                        jj = y + j
                        num = board[ii][jj]
                        if num == '.':
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
        return True
        
            

        