class Node:
    def __init__(self, val=0, next=None, prev=None, key=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache: # LEAST recently used, not last recently used
    def __init__(self, capacity: int):
        print("capacity:", capacity)
        self.capacity = capacity
        self.n = 0
        
        self.prehead = Node()
        self.lru = self.prehead
        #self.lruKey = None
        
        self.hValues = {}
        self.hNodes = {}
        #self.lastKey = None

        #self.lru = None
    
    def moveUsedKeyToFront(self, key):
        if self.n < 2:
            return

        node = self.hNodes[key]
        if node == self.lru:
            #print("Q", self.lru.val)
            #node.prev = self.lru
            self.lru = node.prev
            #print("QQ", self.lru.val)
        #if key == self.lruKey:


        # disconnect other nodes from this one
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        # connect this node at head
        node.prev = self.prehead
        node.next = self.prehead.next

        # connect other nodes to this one
        if self.prehead.next:
            self.prehead.next.prev = node
        self.prehead.next = node

    def get(self, key: int) -> int:
        print("get", key)
        #self.lru = key
        if key in self.hValues:
            self.moveUsedKeyToFront(key)
            return self.hValues[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        print("put", key, value)
        if key not in self.hValues:
            newNode = Node(val=value, key=key)
            if self.n == self.capacity:
                #deleteKey = self.prehead.next.val
                #if key > 2:
                    #print("AAA", self.prehead, self.prehead.next.val, self.prehead.next.next.val, self.prehead.next.next.next)
                    #print("AABB", self.lru.val)
                self.lru.prev.next = None
                deleteKey = self.lru.key
                if self.n == 1:
                    self.lru = newNode
                else:
                    self.lru = self.lru.prev
                #self.hNodes[deleteKey].prev.next = None
                del self.hValues[deleteKey]
                del self.hNodes[deleteKey]
                #self.prehead.next = self.prehead.next.next

                #if key > 2:
                    #print("CCC", self.prehead, self.prehead.next) #.val, self.prehead.next.next.val, self.prehead.next.next.next)
            else:
                self.n += 1
                if self.n == 1:
                    self.lru = newNode
            #self.last.next = Node(key)
            self.hValues[key] = value
            self.hNodes[key] = newNode
            
            newNode.next = self.prehead.next
            newNode.prev = self.prehead
            if self.prehead.next:
                self.prehead.next.prev = newNode
            self.prehead.next = newNode
            #self.last = self.last.next
            #self.moveUsedKeyToFront(True)

            #if key > 2:
                #print("BBB", self.prehead, self.prehead.next.val, self.prehead.next.next) #.val, self.prehead.next.next.next)
        else:
            # change value, but node is same
            self.hValues[key] = value
            #self.hNodes[key] = 
            self.moveUsedKeyToFront(key)

        #self.lru = key
        
