class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        l = len(deck)
        tbf = l
        d = [0]*l
        deck.sort()
        i = 0
        while(tbf>0):
            d[i]=deck[l-tbf]
            tbf=tbf-1
            if(tbf>1):
                while(d[i]!=0):
                    i=(i+1)%l
                i=(i+1)%l
            while(d[i]!=0 and tbf>0):
                i=(i+1)%l
        return d
  
