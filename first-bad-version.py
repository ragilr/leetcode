# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binSearch(0,n,n+1)
    
    def binSearch(self,l,r,s):
        if(l>r):
            return 2**10000
        mid = (l+r)//2
        if(isBadVersion(mid)):
            small = min(s,mid)
            return min(self.binSearch(l,mid-1,small),mid)
        return min(self.binSearch(mid+1,r,s),s)
            
            
        