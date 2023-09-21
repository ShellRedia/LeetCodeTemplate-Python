class RerootingDP:
    def __init__(self, n:int, edges=[], undirected=True):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.undirected = undirected
        for x, y, w in edges: self.add_edge(x, y, w)
    
    def add_edge(self, x, y, w):
        self.g[x].append((y, w))
        self.g[y].append((x, w * 2 * int(self.undirected) - 1))

    def get_result(self) -> list[int]:
        result, size = [0] * self.n,  [1] * self.n
        # ** 专心计算0号节点的结果 **
        def dfs(x: int, fa: int, depth: int) -> None:
            result[0] += depth  # depth 为 0 到 x 的距离
            for y, w in self.g[x]:  # 遍历 x 的邻居 y
                if y != fa:  # 避免访问父节点
                    dfs(y, x, depth + w)  # x 是 y 的父节点
                    size[x] += size[y]  # 累加 x 的儿子 y 的子树大小
        dfs(0, -1, 0)  # 0 没有父节点
        # ** 只需要考虑相邻节点 x 和 y 的相对关系即可 **
        def reroot(x: int, fa: int) -> None:
            for y, w in self.g[x]:  # 遍历 x 的邻居 y
                if y != fa:  # 避免访问父节点
                    result[y] = result[x] + self.n - 2 * size[y] 
                    reroot(y, x)  # x 是 y 的父节点
        reroot(0, -1)  # 0 没有父节点
        return result

# rerooting_dp = RerootingDP(n=n, edges=edges, undirected=True)
# res_lst = rerooting_dp.get_result()
