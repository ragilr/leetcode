class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        ret = []
        def helper(i,sel):
            print(i,sel)
            if i==len(digits):
                ret.append(sel)
                return
            for c in phone[digits[i]]:
                helper(i+1,sel+c)
        if len(digits)>0:
            helper(0,'')
        return ret