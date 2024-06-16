# 用於單點更新，區間求和
class FenwickTree:
    def __init__(self, x):
        if isinstance(x, int):
            self.ft = [0] * x
            self.size = x
        else:
            self.ft = x
            self.size = len(x)
            for i in range(self.size):
                j = i | (i + 1)
                if j < self.size:
                    x[j] += x[i]
 
    def update(self, i, val):
        while i < self.size:
            self.ft[i] += val
            i += self.lowbit(i)
 
    def queryRange(self, l, r): # 要用 prefix sum 的概念來想，所以 [l, r] 的前綴和 = queryRange(l-1, r)
        if l >= r:
            return 0
        return self.query(r) - self.query(l)

    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.ft[i]
            i -= self.lowbit(i)
        return ret

    def lowbit(self, i):
        return i & (-i)