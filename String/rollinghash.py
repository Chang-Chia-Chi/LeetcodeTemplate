    def rolling_hash(self, s: str, window_size: int,
                            base1: int = 26, mod1: int = 10**9 + 7,
                            base2: int = 29, mod2: int = 10**9 + 9) -> List[Tuple[int, int]]:
        n = len(s)
        if window_size > n:
            return []

        power1 = [1] * (n + 1)
        power2 = [1] * (n + 1)
        for i in range(1, n + 1):
            power1[i] = (power1[i - 1] * base1) % mod1
            power2[i] = (power2[i - 1] * base2) % mod2


        hash_values = [None] * (n - window_size + 1)
        current_hash1 = 0
        current_hash2 = 0
        for i in range(window_size):
            current_hash1 = (current_hash1 * base1 + ord(s[i])) % mod1
            current_hash2 = (current_hash2 * base2 + ord(s[i])) % mod2

        hash_values[0] = (current_hash1, current_hash2)

        for i in range(1, n - window_size + 1):
            current_hash1 = (current_hash1 - power1[window_size - 1] * ord(s[i - 1])) % mod1
            current_hash1 = (current_hash1 * base1 + ord(s[i + window_size - 1])) % mod1
            current_hash2 = (current_hash2 - power2[window_size - 1] * ord(s[i - 1])) % mod2
            current_hash2 = (current_hash2 * base2 + ord(s[i + window_size - 1])) % mod2

            hash_values[i] = (current_hash1, current_hash2)

        return hash_values