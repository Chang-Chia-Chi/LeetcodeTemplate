# Ref: 灵茶山艾府 https://leetcode.cn/circle/discuss/mDfnkW/
# 組合數預處理，注意 MOD 必需要是質數
class Solution:
    def solve():
        def comb(n: int, m: int) -> int:
            return fac[n] * inv_f[m] * inv_f[n - m] % MOD if 0 <= m <= n else 0

        MOD = 1_000_000_007 # Leetcode 常見的模數
        MX = 100_001 # 依照題意調整範圍

        fac = [0] * MX
        fac[0] = 1
        for i in range(1, MX):
            fac[i] = fac[i - 1] * i % MOD

        inv_f = [0] * MX
        inv_f[-1] = pow(fac[-1], -1, MOD)
        for i in range(MX - 1, 0, -1):
            inv_f[i - 1] = inv_f[i] * i % MOD