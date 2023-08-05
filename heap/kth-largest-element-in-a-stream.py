class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.klarge = nums[-k:]
        heapq.heapify(self.klarge)
        self.k = k

    def add(self, val: int) -> int:
        if len(self.klarge) < self.k:
            heapq.heappush(self.klarge,val)
        elif len(self.klarge)>0 and val>self.klarge[0]:
            heapq.heapreplace(self.klarge,val)
        return self.klarge[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)