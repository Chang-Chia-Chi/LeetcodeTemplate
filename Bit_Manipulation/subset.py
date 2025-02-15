def getSubsets(self, state):
    subset = state
    while subset:
        yield subset
        subset = (subset - 1) & state