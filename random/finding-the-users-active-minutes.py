class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        userActivity = dict()
        for log in logs:
            user,time = log[0],log[1]
            if not user in userActivity:
                userActivity[user] = set()
            userActivity[user].add(time)
        count = Counter(map(lambda x : len(x),userActivity.values()))
        ret = [0]*k
        for i in range(k):
            ret[i]=count[i+1]
        return ret