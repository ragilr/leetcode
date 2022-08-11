class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def findPath(m,n,d):
            a=str(m)+",",str(n)
            if a in d:
                return d[a]
            b=str(n)+","+str(m)
            if b in d:
                return d[b]

            if m ==0 or n==0:
                return 0
            if m==1 and n==1:
                return 1
            d[a]=findPath(m-1,n,d)+findPath(m,n-1,d)
            d[b]=d[a]
            return d[a]
        return findPath(m,n,dict())
        