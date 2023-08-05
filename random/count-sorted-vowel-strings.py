class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        vowels = ['a','e','i','o','u']
        d=dict()
        def numofways(l,last_char):
            key = str(l)+','+str(last_char)
            if key in d:
                return d[key]
            if l==0:
                return 1
            tot = 0
            for i in range(last_char,5):
                tot+=numofways(l-1,i)
            d[key]=tot
            return tot
        
        return numofways(n,0)
        