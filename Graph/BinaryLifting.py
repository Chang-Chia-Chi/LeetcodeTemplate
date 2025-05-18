class BinaryLifting:
    def __init__(self, n, adj, root=0):
        """
        n     : number of nodes (0..n-1)
        adj   : adjacency list, adj[u] = list of neighbors of u
        root  : root of the tree (default 0)
        """
        self.n = n
        self.LOG = (n-1).bit_length()
        self.parent = [[-1]*n for _ in range(self.LOG)]
        self.depth  = [0]*n
        self.adj = adj
        self._dfs(root, -1, 0)

        for k in range(self.LOG-1):
            for v in range(n):
                p = self.parent[k][v]
                self.parent[k+1][v] = -1 if p<0 else self.parent[k][p]

    def _dfs(self, u, p, d):
        self.parent[0][u] = p
        self.depth[u] = d
        for v in self.adj[u]:
            if v == p: continue
            self._dfs(v, u, d+1)

    def lca(self, a, b):
        """
        Returns the lowest common ancestor of a and b
        """
        if self.depth[a] < self.depth[b]:
            a, b = b, a
 
        diff = self.depth[a] - self.depth[b]
        for k in range(self.LOG):
            if diff >> k & 1:
                a = self.parent[k][a]
        if a == b:
            return a
 
        for k in reversed(range(self.LOG)):
            if self.parent[k][a] != self.parent[k][b]:
                a = self.parent[k][a]
                b = self.parent[k][b]

        return self.parent[0][a]
