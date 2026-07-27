class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
       # return true if the word is present in the grid 
       # is the board small?   
       # only proceed if next index of word is available.
       # for cat -> require C, then A, then T. So well need to index into owrd as well.
       # set of visited paths 
       # edges
       # what choices are made?
       # down or right
        m = len(board)
        n = len(board[0])
        k = len(word)
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c, wordIdx):
            if wordIdx == k:
                return True

            if (r, c) in visited:
                return False
            if r < 0 or r >= m or c <0 or c>=n:
                return False
            if board[r][c] != word[wordIdx]:
                return False
            
            visited.add((r, c))
            result = False
            for dr, dc in dirs:
                rr = dr + r
                cc = dc + c
                result = result or  dfs(rr, cc, wordIdx+1) 
            visited.discard((r, c))
            return result
        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False

                

