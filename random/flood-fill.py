class Solution:
    def isValidPixel(self,image: List[List[int]], sr: int, sc: int)-> bool:
        return (sr>-1 and sr<len(image) and sc>-1 and sc<len(image[0]))
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initColor = image[sr][sc]
        image[sr][sc]=color
        
        if self.isValidPixel(image,sr+1,sc) and image[sr+1][sc]==initColor and image[sr+1][sc]!=color:
            self.floodFill(image,sr+1,sc,color)
        if self.isValidPixel(image,sr,sc+1) and image[sr][sc+1]==initColor and image[sr][sc+1]!=color:
            self.floodFill(image,sr,sc+1,color)
        if self.isValidPixel(image,sr-1,sc) and image[sr-1][sc]==initColor and image[sr-1][sc]!=color:
            self.floodFill(image,sr-1,sc,color)
        if self.isValidPixel(image,sr,sc-1) and image[sr][sc-1]==initColor and image[sr][sc-1]!=color:
            self.floodFill(image,sr,sc-1,color)
        return image
        