class Node:
    __slots__ = 'val', 'todo'

class LazySegmentTree:
    # 懶惰標記的初始值
    _TODO_INIT = 0  # **根據題目修改**

    def __init__(self, n: int, init_val=0):
        # 線段樹維護一個長度為 n 的陣列（下標從 0 到 n-1），元素初始值為 init_val
        # init_val 可以是 list 或 int
        # 如果是 int，則會建立一個 list
        if isinstance(init_val, int):
            init_val = [init_val] * n
        self._n = n
        self._tree = [Node() for _ in range(2 << (n - 1).bit_length())]
        self._build(init_val, 1, 0, n - 1)

    # 合併兩個 val
    def _merge_val(self, a: int, b: int) -> int:
        return a + b  # **根據題目修改**

    # 合併兩個懶惰標記
    def _merge_todo(self, a: int, b: int) -> int:
        return a + b  # **根據題目修改**

    # 把懶惰標記套用到 node 子樹（本例為區間加）
    def _apply(self, node: int, l: int, r: int, todo: int) -> None:
        cur = self._tree[node]
        # 計算 tree[node] 區間的整體變化
        cur.val += todo * (r - l + 1)  # **根據題目修改**
        cur.todo = self._merge_todo(todo, cur.todo)

    # 將當前節點的懶惰標記向下傳遞給左右兒子
    def _spread(self, node: int, l: int, r: int) -> None:
        todo = self._tree[node].todo
        if todo == self._TODO_INIT:  # 沒有需要傳遞的資訊
            return
        m = (l + r) // 2
        self._apply(node * 2, l, m, todo)
        self._apply(node * 2 + 1, m + 1, r, todo)
        self._tree[node].todo = self._TODO_INIT  # 傳遞完畢

    # 將左右子節點的 val 合併至當前節點
    def _maintain(self, node: int) -> None:
        self._tree[node].val = self._merge_val(
            self._tree[node * 2].val,
            self._tree[node * 2 + 1].val
        )

    # 使用 a 初始化整棵線段樹
    # 時間複雜度 O(n)
    def _build(self, a: List[int], node: int, l: int, r: int) -> None:
        self._tree[node].todo = self._TODO_INIT
        if l == r:  # 葉節點
            self._tree[node].val = a[l]  # 初始化葉節點的值
            return
        m = (l + r) // 2
        self._build(a, node * 2, l, m)      # 初始化左子樹
        self._build(a, node * 2 + 1, m + 1, r)  # 初始化右子樹
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, ql: int, qr: int, f: int) -> None:
        if ql <= l and r <= qr:  # 當前子樹完全在 [ql, qr] 區間內
            self._apply(node, l, r, f)
            return
        self._spread(node, l, r)
        m = (l + r) // 2
        if ql <= m:  # 更新左子樹
            self._update(node * 2, l, m, ql, qr, f)
        if qr > m:   # 更新右子樹
            self._update(node * 2 + 1, m + 1, r, ql, qr, f)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:  # 當前子樹完全在 [ql, qr] 區間內
            return self._tree[node].val
        self._spread(node, l, r)
        m = (l + r) // 2
        if qr <= m:  # [ql, qr] 完全在左子樹
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:   # [ql, qr] 完全在右子樹
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_res = self._query(node * 2, l, m, ql, qr)
        r_res = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_val(l_res, r_res)

    # 對 [ql, qr] 區間內的每個 a[i] 套用 f
    # 0 <= ql <= qr <= n-1
    # 時間複雜度 O(log n)
    def update(self, ql: int, qr: int, f: int) -> None:
        self._update(1, 0, self._n - 1, ql, qr, f)

    # 回傳將 a[i] 合併後的結果，其中 i 在閉區間 [ql, qr] 中
    # 0 <= ql <= qr <= n-1
    # 時間複雜度 O(log n)
    def query(self, ql: int, qr: int) -> int:
        return self._query(1, 0, self._n - 1, ql, qr)


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/discuss/post/mOr1u6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。