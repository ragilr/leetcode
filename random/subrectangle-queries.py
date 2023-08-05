
class SubrectangleQueries(object):
    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.original = rectangle
        # print self.original
        self.rect=[]
        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        self.rect.append([row1,col1,row2,col2,newValue])
        # print self.rect
        

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        # print row,col
        # print self.original
        for r in reversed(self.rect):
            # print r,type(r)
            if(row>=r[0] and row<=r[2] and col>=r[1] and col<=r[3]):
                return r[4]
        return self.original[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
