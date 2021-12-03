class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            # print(board[i])
            d = dict()
            for n in board[i]:
                # print(n)
                if n=='.':
                    continue
                elif not n in d:
                    d[n]=1
                else:
                    return False
        for j in range(9):
            d = dict()
            for i in range(9):
                n = board[i][j]
                if n=='.':
                    continue
                elif not n in d:
                    d[n]=1
                else:
                    return False
                    
        for i in range(0,8,3):
            for j in range(0,8,3):
                d = dict()
                for k in range(3):
                    for l in range(3):
                        n = board[i+k][j+l]
                        if n=='.':
                            continue
                        elif not n in d:
                            d[n]=1
                        else:
                            return False
        return True