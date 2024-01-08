class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ret = []
        def helper(open_br,close_br,s):
            if open_br == n and close_br == n:
                ret.append(s)
                return
            if open_br>n or close_br>n or close_br>open_br:
                return
            if open_br>close_br:
                helper(open_br+1,close_br,s+'(')
                helper(open_br,close_br+1,s+')')
            else:
                helper(open_br+1,close_br,s+'(')

        helper(0,0,'')
        return ret