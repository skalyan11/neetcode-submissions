class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hm = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.capacity = capacity
        self.tail.prev = self.head


    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        node.next, nxt.prev = nxt, node



    def get(self, key: int) -> int:
        if key in self.hm:
            self.remove(self.hm[key])
            self.insert(self.hm[key])
            return self.hm[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.hm[key] = node
            self.insert(node)


        if len(self.hm) > self.capacity:
             lru = self.head.next
             self.remove(lru)
             del self.hm[lru.key]
            
