# 直接算出 [l, r] 區間內有多少個數字滿足條件
def digitDP(l, r):
    low = list(map(int, str(l)))
    high = list(map(int, str(r)))
    n = len(high)
    diff_lh = n - len(low)

    @cache
    def dfs(i: int, m: int, s: int, limit_low: bool, limit_high: bool) -> int:
        if i == n:
            # return your logic
            return 1 if s and m % s == 0 else 0

        lo = low[i - diff_lh] if limit_low and i >= diff_lh else 0 # tight low
        hi = high[i] if limit_high else 9 # tight high

        res = 0
        if limit_low and i < diff_lh: # 代表前面的位數都是 0
            res += dfs(i + 1, 1, 0, True, False)  # 繼續往下一位數，但是前面的位數都是 0
            d = 1  # 下面的 for 迴圈從 1 開始
        else:
            d = lo
    
        # 枚舉下一位數的值
        for d in range(d, hi + 1):
            # dfs(i + 1, your logic, your logic, limit_low and d == lo logic, limit_high and d == hi logic)
            res += dfs(i + 1, m * d, s + d, limit_low and d == lo, limit_high and d == hi)
        return res

    # dfs(0, your logic, your logic, True, True)
    return dfs(0, 1, 0, True, True) 