class Node:
    def __init__(self, val):
        self.val = val
        self.size = 1
        self.parent = self


    def merge(self, other):
        self.size += other.size
        other.parent = self


class DisjointSet:
    def __init__(self):
        self.nodesMap = {}
        self.sets = 0


    def inSet(self, val):
        return val in self.nodesMap


    def fetchNode(self, val):
        isNew = False
        if val not in self.nodesMap:
            isNew = True
            self.sets += 1
            self.nodesMap[val] = Node(val)
        return (self.nodesMap[val], isNew)


    def find(self, node):
        if node.parent is node:
            return node
    
        node.parent = self.find(node.parent)
        return node.parent


    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 != p2:
            self.sets -= 1
            p2.merge(p1)