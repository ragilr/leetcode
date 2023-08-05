class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d=set()
        for a in arr:
            if 2*a in d or a/2 in d:
                return True
            d.add(a)
        return False