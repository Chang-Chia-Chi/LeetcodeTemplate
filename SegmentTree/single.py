class SegmentTreeNode:
    def __init__(self, start, end, val):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        self.__initHelper(start, end, val)

    def __initHelper(self, start, end, val):
        if (start == end):
            self.__updateInfoLeaf(val[self.start])
            return
        
        mid = start + (end-start)//2
        if self.left is None:
            self.left = SegmentTreeNode(start, mid, val)
            self.right = SegmentTreeNode(mid+1, end, val)
            self.__updateInfoParent()


    def __updateInfoLeaf(self, val):
        # Modify logic here
        self.info = val


    def __updateInfoParent(self):
        # Modify logic here
        self.info = self.left.info + self.right.info


    def updateSingle(self, start, val):
        if start < self.start or start > self.end:
            return
        
        if (start <= self.start and self.end <= start):
            self.__updateInfoLeaf(val[self.start])
            return

        if self.left:
            self.left.updateSingle(start, val)
            self.right.updateSingle(start, val)
            self.__updateInfoParent()

    def queryRange(self, start, end):
        if (end < self.start or start > self.end):
            return 0
        
        if (start <= self.start and self.end <= end):
            return self.info # Modify logic here
        
        if self.left:
            result = self.left.queryRange(start, end) + self.right.queryRange(start, end)
            return result
        
        return self.info # Modify logic here
