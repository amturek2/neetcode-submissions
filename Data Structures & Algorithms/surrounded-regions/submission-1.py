class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque
        # take the set difference of 0 connected to the border
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(1, 0), (-1, 0), 
                      (0,1), (0,-1)]
        q = deque()
        visited = set()
        def isEdgePiece(row, col):
            return (row == ROWS - 1) or (col == COLS - 1) or (row == 0 )or (col == 0)

        def bfs(q, visited):
            # run bfs creating a list - if you hit an edge piece destroy the list - then add the list to set
            while q:
                r, c = q.popleft()
                for d in directions: 
                    nr, nc = r + d[0], c + d[1]
                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and 
                        (nr,nc) not in visited and 
                        board[nr][nc] == "O"):             
                        q.append((nr, nc))
                        visited.add((nr,nc))

            return


   
        for row in range(ROWS):
            for col in range(COLS):
                # if board[row][col] == "O" and (row,col) not in visited:
                if board[row][col] == "O" and isEdgePiece(row,col):
                    q.append((row,col))
                    visited.add((row,col))
        bfs(q, visited)
        for row in range(ROWS):
            for col in range(COLS):
                # if board[row][col] == "O" and (row,col) not in visited:
                if board[row][col] == "O" and (row, col) not in visited:
                   board[row][col] = "X"
