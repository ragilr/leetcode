class Node:
    def __init__(self,k):
        self.key = k
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = None
        self.tail = None
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        # print("get",key)
        # self.printLru()
        if not key in self.cache:
            return -1
        value,node = self.cache[key]
        self.refreshLru(node,value)
        # self.printLru()
        return value
    
    def haveCapacity(self) -> bool:
        return len(self.cache) < self.capacity
        

    def put(self, key: int, value: int) -> None:
        # print("put",key)
        # self.printLru()
        if not key in self.cache:   #add to cache
            if not self.haveCapacity():
                self.removeFromLru()
            node = self.addToLru(key)
        else:   #update cache value
            _, node = self.cache[key]
            self.refreshLru(node, value)
            # self.cache[key] = (value,node)
        self.cache[key] = (value,node)
        # self.printLru()
    
    def addToLru(self, key:int) -> Node:
        node = Node(key)
        if self.head == None: #first element
            self.head = node
            self.tail = node
        else:
            nxt = self.head
            nxt.prev = node
            node.next = nxt
            self.head = node
        return node
    
    def removeFromLru(self) -> None:
        del self.cache[self.tail.key]
        if self.head == self.tail: #last element
            self.head = self.tail = None            
            return
        tail = self.tail.prev
        tail.next = None
        self.tail = tail
        
    
    def refreshLru(self, node:Node, val:int) -> None:
        if self.head == node: #already top element
            return
        if self.tail == node:
            tail = node.prev
            tail.next = None
            self.tail = tail
        else:
            left = node.prev
            right = node.next
            left.next = right
            right.prev = left
        nxt = self.head
        node.next = nxt
        nxt.prev = node
        self.head = node

    def printLru(self) -> None:
        node = self.head
        while node:
            print(node.key,'->' ,end='',sep='')
            node = node.next
        print("")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)