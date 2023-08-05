class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        num_of_team = len(votes[0])
        num_of_votes = len(votes)
        ranks = dict()

        for vote in votes[0]:
            ranks[vote]=[num_of_votes]*num_of_team
        
        for i in range(num_of_team):
            for vote in votes:
                team=vote[i]
                ranks[team][i]-=1
        
        # print(ranks)
        ranks = sorted(ranks.items(), key = lambda x: (x[1],x[0]))
        ret = [team[0] for team in ranks]
        return "".join(ret)