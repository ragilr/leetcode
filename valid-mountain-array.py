class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        i = 1
        up=False
        down=False
        while i < len(arr) and arr[i-1]<arr[i]:
            i=i+1
            up=True
        while i < len(arr) and arr[i-1]>arr[i]:
            i=i+1
            down=True
        return len(arr)==i and up and down