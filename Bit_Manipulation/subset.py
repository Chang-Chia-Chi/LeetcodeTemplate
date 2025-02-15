def getSubsets(self, state):
    subset = state
    while subset:
        yield subset
        subset = (subset - 1) & state


# Iterate all the m-bit state where there are k 1-bits.
def gospersHack(self, m, k, state):
    state = (1 << k) - 1
    while state < (1 << m):
        yield state
        c = state & -state
        r = state + c
        state = (((r ^ state) >> 2) / c) | r