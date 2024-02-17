class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxheap = []
        prev = heights[0]
        for i in range(len(heights)):
            gain = heights[i]-prev
            prev=heights[i]
            # print(heights[i],gain,ladders,bricks)
            if gain<=0:
                continue
            heapq.heappush(maxheap,-gain)
            bricks = bricks-gain
            if bricks<0 and ladders:
                bricks=bricks-(heapq.heappop(maxheap))
                ladders-=1
            elif bricks<0:
                return i-1
        return len(heights)-1