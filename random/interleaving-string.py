import copy

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        row = [-1]*(len(s2)+1)
        self.mat =[copy.deepcopy(row)]*(len(s1)+1)
        if(len(s3)!=len(s1)+len(s2)):
            return False
        return self.checkInterLeaving(s1, s2, s3)
    
    def checkInterLeaving(self, s1: str, s2:str, s3:str) -> bool:
        ls1=len(s1)
        ls2=len(s2)
        ls3=len(s3)
        if(not self.mat[ls1][ls2]!=-1):
            return self.mat[ls1][ls2]
        if(ls1+ls2!=ls3):
            self.mat[ls1][ls2]=False
            return False
        if(ls1==0 and ls2==0 and ls3==0):
            return True
        if(ls3==0 and (ls2!=0 or ls1!=0)):
            return False
        a=False
        b=False
        if(ls1>0 and s1[0]==s3[0]):
            a = self.checkInterLeaving(s1[1:], s2, s3[1:])
        if(ls2>0 and s2[0]==s3[0]):
            b = self.checkInterLeaving(s1, s2[1:], s3[1:])
        self.mat[ls1][ls2]=a or b
        return a or b