class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedMap = dict()
        for i,pos in enumerate(position):
            speedMap[pos]=speed[i]
        c = 0
        mx_time = float('-inf')
        position.sort(reverse=True)
        # print(position)
        for pos in position:
            time = (target-pos)/speedMap[pos]
            if time>mx_time:
                mx_time = time
                c+=1            
        return c