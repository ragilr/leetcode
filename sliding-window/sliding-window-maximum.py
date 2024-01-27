class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # using heap
        # h = []
        # ret = []
        # for i,n in enumerate(nums):
        #     heapq.heappush(h,(-n,i))
        #     mx,idx = h[0][0],h[0][1]
        #     while i-idx>=k:
        #         # print("inside")
        #         heapq.heappop(h)
        #         mx,idx = h[0][0],h[0][1]
        #     if len(h)>=k:
        #         # print("adding",-mx)
        #         ret.append(-mx)
        #     # print(ret,h)
        # return ret

        # deque based
        q = deque()
        ret = []
        for i,n in enumerate(nums):
            while q and q[-1][0]<n:
                q.pop()
            q.append([n,i])
            while q and i-q[0][1]>=k:
                q.popleft()
            if i+1>=k:
                ret.append(q[0][0])
        return ret