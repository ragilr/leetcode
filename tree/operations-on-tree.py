class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        child = {}
        for i,p in enumerate(parent):
            if p in child:
                child[p].append(i)
            else:
                child[p] = [i]
        self.child = child
        self.locks = {}
        # print(self.parent)
        # print(self.child)


    def lock(self, num: int, user: int) -> bool:
        if num in self.locks:
            return False
        self.locks[num]=user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locks and self.locks[num]==user:
            del self.locks[num]
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locks:
            return False
        n = num
        while n!=-1:
            n=self.parent[n]
            if n in self.locks:
                return False
        descen = []
        q = deque([num])        
        while q:
            item = q.popleft()
            if item in self.locks:
                descen.append(item)
            if item in self.child:
                for c in self.child[item]:
                    q.append(c)
        if len(descen)==0:
            return False
        # print(descen)
        for d in descen:
            del self.locks[d]
        self.locks[num]=user
        return True

        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)