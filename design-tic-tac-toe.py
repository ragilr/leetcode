class TicTacToe:
    
    def __init__(self, n: int):
        self.r = []
        self.c = []
        self.diag = [0,0]
        self.cdiag = [0,0]
        self.n = n
        for i in range(n):
            self.r.append([0,0])
            self.c.append([0,0])

    def move(self, row: int, col: int, player: int) -> int:
        if(self.r[row][0]==0 or self.r[row][0]==player):
            self.r[row][0] = player
            self.r[row][1] += 1
        else:
            self.r[row][0]=-1
            self.r[row][1]=-1
        if(self.c[col][0]==0 or self.c[col][0]==player):
            self.c[col][0] = player
            self.c[col][1] += 1
        else:
            self.c[col][0]=-1
            self.c[col][1]=-1
            
        if(row==col): #dia
            if(self.diag[0]==0 or self.diag[0]==player):
                self.diag[0] = player
                self.diag[1] += 1
        
        if(row+col == self.n-1):
            if(self.cdiag[0]==0 or self.cdiag[0]==player):
                self.cdiag[0] = player
                self.cdiag[1] += 1
        
        # print(self.r,self.c,self.diag,self.cdiag)
        if(self.r[row][1]==self.n or self.c[col][1]==self.n or self.diag[1]==self.n or self.cdiag[1]==self.n):
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)