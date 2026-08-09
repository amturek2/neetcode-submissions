class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque
     
        # connected if none of the 0 cells are on the edge 
        # 
        # if you reach an edge piece in your traversal - go back 
        
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(1, 0), (-1, 0), (0,1), (0,-1)]
        colorSet = set()

        def isEdgePiece(row, col):
            return (row == ROWS - 1) or (col == COLS - 1) or (row == 0 )or (col == 0)

        def bfs(srcRow, srcCol):
            nonlocal colorSet
        # run bfs creating a list - if you hit an edge piece destroy the list - then add the list to set
            q = deque()
            q.append((srcRow, srcCol))
            visited = set()
            visited.add((srcRow, srcCol))
            currentList = []
            if isEdgePiece(srcRow, srcCol): 
                return 
            currentList.append((srcRow, srcCol))

            while q:
                r, c = q.popleft()
                
                for d in directions: 
                    nr, nc = r + d[0], c + d[1]
                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and 
                        (nr,nc) not in visited and 
                        board[nr][nc] == "O"):
                        
                        if isEdgePiece(nr, nc):
                            return 
                        if (nr, nc) in colorSet: 
                            colorSet.update(currentList)
                            return
                        
                        currentList.append((nr, nc))
                        q.append((nr, nc))
                        visited.add((nr,nc))
            colorSet.update(currentList)
            return



        for row in range(ROWS):
            for col in range(COLS):
                # if board[row][col] == "O" and (row,col) not in visited:
                if board[row][col] == "O":
                    bfs(row,col)

        for r, c in colorSet: 
            board[r][c] = "X"

