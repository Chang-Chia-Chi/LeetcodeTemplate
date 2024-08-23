class SegmentTreeNode:
    def __init__(self, start, end, val):
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        self.tag = 0
        self.delta = 0
        self.__initHelper(start, end, val)

    def __initHelper(self, start, end, val):
        if isinstance(val, list):
            if start == end:
                self.__updateInfoLeaf(val[self.start])
                return

            mid = start + (end - start) // 2
            self.left = SegmentTreeNode(start, mid, val)
            self.right = SegmentTreeNode(mid + 1, end, val)
            self.__updateInfoParent()
        else:
            self.info = val
            if start == end:
                return

            mid = start + (end - start) // 2
            self.left = SegmentTreeNode(start, mid, val)
            self.right = SegmentTreeNode(mid + 1, end, val)
            self.__updateInfoParent()

    def __updateInfoLeaf(self, val):
        self.info = val

    def __updateInfoParent(self):
        self.info = self.left.info + self.right.info

    def pushDown(self):
        if self.tag == 1 and self.left:
            self.left.info += self.delta * (self.left.end - self.left.start + 1)
            self.left.delta += self.delta
            self.right.info += self.delta * (self.right.end - self.right.start + 1)
            self.right.delta += self.delta
            self.left.tag = 1
            self.right.tag = 1
            self.tag = 0
            self.delta = 0

    def updateRangeBy(self, start, end, val):
        if end < self.start or start > self.end:
            return

        if start <= self.start and self.end <= end:
            self.info += val * (self.end - self.start + 1)
            self.delta += val
            self.tag = 1
            return

        if self.left:
            self.pushDown()
            self.left.updateRangeBy(start, end, val)
            self.right.updateRangeBy(start, end, val)
            self.__updateInfoParent()

    def queryRange(self, start, end):
        if end < self.start or start > self.end:
            return 0

        if start <= self.start and self.end <= end:
            return self.info

        if self.left:
            self.pushDown()
            result = self.left.queryRange(start, end) + self.right.queryRange(start, end)
            return result

        return self.info