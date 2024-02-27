class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])
        noflip = set()
        def dfs(x,y):
            if x<0 or y<0 or x==r or y==c or board[x][y]=='X' or (x,y) in noflip:
                return
            noflip.add((x,y))
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
        for i in range(r):
            if board[i][0] and (i,0) not in noflip:
                dfs(i,0)
            if board[i][c-1] and (i,c-1) not in noflip:
                dfs(i,c-1)
        for j in range(c):
            if board[0][j] and (0,j) not in noflip:
                dfs(0,j)
            if board[r-1][j] and (r-1,j) not in noflip:
                dfs(r-1,j)
        # print(board)
        for i in range(r):
            for j in range(c):
                if board[i][j]=='O' and (i,j) not in noflip:
                    board[i][j]='X'