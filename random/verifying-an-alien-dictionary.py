class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for idx, c in enumerate(order):
            order_map[c]=idx
        for i in range(len(words)-1):
            a,b=words[i],words[i+1]
            for j in range(len(a)):
                if j == len(b):
                    return False
                if a[j]!=b[j]:
                    if order_map[a[j]]>order_map[b[j]]:
                        return False
                    break
        return True