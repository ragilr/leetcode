class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        j=len(people)-1
        c=0
        n = 0
        while i<j:
            # print("start",i,j,c)
            if people[i]+people[j]<=limit:
                i+=1
                n+=1
            j-=1
            c+=1
            n+=1
            # print("end",i,j,c)
        if n!=len(people):
            c+=1
        return c