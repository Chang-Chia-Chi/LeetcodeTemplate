class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeMap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def isHead(self, node): return node.prev is self.head or node.prev is None
    
    def isTail(self, node): return node.next is self.tail or node.next is None

    def search(self, key):
        return self.nodeMap.get(key, None)

    # note that it's reverse order of insertion
    # e.g: [1, 2, 3], when you go through the list, you will get 3, 2, 1
    def insert(self, node):
        self.nodeMap[node.key] = node

        headNext = self.head.next
        node.next= headNext
        headNext.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1

    def remove(self, node):
        if node.key not in self.nodeMap:
            return
        
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev
        del self.nodeMap[node.key]
        self.size -= 1
    
    def pop(self):
        last = self.tail.prev
        if last is self.head:
            return
        
        self.remove(last)
        return last