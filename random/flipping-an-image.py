class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        print(image)
        for irow in image:
            irow.reverse()
            for i in range(len(irow)):
                if irow[i]==0:
                    irow[i]=1
                else:
                    irow[i]=0
        return image