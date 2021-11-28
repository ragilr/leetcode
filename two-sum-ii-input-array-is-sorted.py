class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s=0
        e=len(numbers)-1
        # sum = numbers[s]+numbers[e]
        # print(s,e,sum)
        while(s<=e):
            sum = numbers[s]+numbers[e]
            if(target==numbers[s]+numbers[e]):
                return[s+1,e+1]
            elif(target<sum):
                e-=1
            else:
                s+=1
            # print(s,e,sum)
        