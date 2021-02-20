class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        d = dict()
        for i in range(m):
            for j in range(n):
                key = i-j
                if key in d:
                    d[key].append(mat[i][j])
                else:
                    d[key] = [mat[i][j]]
        for key, value in d.items():
            value.sort(reverse=True)
            d[key] = value
        for i in range(m):
            for j in range(n):
                val = d[i-j].pop()
                mat[i][j]=val
        return mat
