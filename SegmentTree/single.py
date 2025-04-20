# 線段樹有兩個下標，一個是線段樹節點的下標，另一個是線段樹維護的區間的下標
# 節點的下標：從 1 開始，如果你想改成從 0 開始，需要把左右兒子下標分別改成 node*2+1 和 node*2+2
# 區間的下標：從 0 開始
class SegmentTree:
    def __init__(self, n: int, init_val=0):
        # 線段樹維護一個長度為 n 的陣列（下標從 0 到 n-1），元素初始值為 init_val
        # init_val 可以是 list 或 int
        # 如果是 int，那麼會建立一個 list
        if isinstance(init_val, int):
            init_val = [init_val] * n
        self._n = n
        self._tree = [0] * (2 << (n - 1).bit_length())
        self._build(init_val, 1, 0, n - 1)

    # 合併兩個 val
    def _merge_val(self, a: int, b: int) -> int:
        return max(a, b)  # **根據題目修改**

    # 將左右兒子的 val 合併到當前節點
    def _maintain(self, node: int) -> None:
        self._tree[node] = self._merge_val(self._tree[node * 2], self._tree[node * 2 + 1])

    # 用 a 初始化線段樹
    # 時間複雜度 O(n)
    def _build(self, a: List[int], node: int, l: int, r: int) -> None:
        if l == r:  # 葉節點
            self._tree[node] = a[l]  # 初始化葉節點的值 # **根據題目修改**
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m)  # 初始化左子樹
        self._build(a, node * 2 + 1, m + 1, r)  # 初始化右子樹
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:  # 葉節點（到達目標）
            # 如果想直接替換，可以寫成 self._tree[node] = val
            self._tree[node] = self._merge_val(self._tree[node], val) # **根據題目修改**
            return
        m = (l + r) // 2
        if i <= m:  # i 在左子樹
            self._update(node * 2, l, m, i, val)
        else:  # i 在右子樹
            self._update(node * 2 + 1, m + 1, r, i, val)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:  # 當前子樹完全在 [ql, qr] 區間內
            return self._tree[node]
        m = (l + r) // 2
        if qr <= m:  # [ql, qr] 完全在左子樹
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:  # [ql, qr] 完全在右子樹
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_res = self._query(node * 2, l, m, ql, qr)
        r_res = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_val(l_res, r_res)

    # 更新 a[i] 為 _merge_val(a[i], val)
    # 時間複雜度 O(log n)
    def update(self, i: int, val: int) -> None:
        self._update(1, 0, self._n - 1, i, val)

    # 回傳用 _merge_val 合併所有 a[i] 的結果，其中 i 在閉區間 [ql, qr] 中
    # 時間複雜度 O(log n)
    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)

    # 取得 a[i] 的值
    # 時間複雜度 O(log n)
    def get(self, i: int) -> int:
        return self._query(1, 0, self._n - 1, i, i)


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/discuss/post/mOr1u6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。