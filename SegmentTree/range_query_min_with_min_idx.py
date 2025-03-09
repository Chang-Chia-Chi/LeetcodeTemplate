"""
線段樹模板，主要用於查找符合條件且索引最小的元素。

使用方法：
    data = [2, 6, 1, 5, 3, 4]
    st = SegmentTree(data)          # 依據原始陣列建立線段樹
    st.update(1, 3)                 # 更新索引 1 的元素為 3
    idx = st.find_first(0, 5)       # 從索引 0 開始查找第一個值 >= 5 的元素
    print("符合條件的最小索引:", idx)

原理說明：
1. 線段樹建立時，將原始陣列的每個元素存放在葉節點，並且這些葉節點的位置與原始陣列索引一一對應。
2. 每個內部節點儲存其左右子樹區間內的最大值，因此我們可以迅速判斷一個區間中是否存在滿足條件（大於等於 threshold）的元素。
3. 查詢過程中，find_first(l, threshold) 從根節點開始遞迴搜尋：
   - 如果當前節點所代表的區間完全不在查詢範圍內（即右邊界 <= l），或該區間內的最大值小於 threshold，則直接返回 -1（進行剪枝）。
   - 當節點區間長度為 1（即葉節點），表示此時已定位到單一元素，直接返回其索引。
   - 遞迴時優先查詢左子樹（左側覆蓋較小索引），如果左子樹找到了符合條件的元素，則返回該結果；否則再查詢右子樹。
   這樣確保了返回的索引是滿足條件中最小的索引。
4. 簡單來說，就是我們使用索引作為區間搜索條件，並將最大值記錄在節點上，我們都先往左走，如果左子樹沒有符合條件的元素，再往右走，確保返回的是最小索引。
"""
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [float('-inf')] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx, value):
        i = idx + self.size
        self.tree[i] = value
        i //= 2
        while i:
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])
            i //= 2

    def find_first(self, l, threshold):
        return self._find_first(1, 0, self.size, l, threshold)
    
    def _find_first(self, idx, left, right, l, threshold):
        if right <= l or self.tree[idx] < threshold:
            return -1
        if right - left == 1:
            return left
        mid = (left + right) // 2
        res = self._find_first(idx * 2, left, mid, l, threshold)
        if res == -1:
            res = self._find_first(idx * 2 + 1, mid, right, l, threshold)
        return res
    
if __name__ == "__main__":
    arr = [1, 3, 2, 5, 7, 6, 4, 8]
    segTree = SegmentTree(arr)
    idx = segTree.find_first(0, 5)
    print(idx) # Output 3