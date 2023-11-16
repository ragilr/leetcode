class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = len(strs[0])
        for string in strs:
            m = min(len(string),m)
        i = 0
        same = True
        while i<m and same:
            c = strs[0][i]
            for string in strs:
                if string[i] != c:
                    return string[:i]
            i+=1
        return strs[0][:m]