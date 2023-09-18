class RerootingDP:
    def __init__(self, n:int, edges: List[List[int]]):
        if n: g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        self.result, size = [0] * n,  [1] * n

        # 专心计算0号节点的结果
        def dfs(x: int, fa: int, depth: int) -> None:
            self.result[0] += depth  # depth 为 0 到 x 的距离
            for y in g[x]:  # 遍历 x 的邻居 y
                if y != fa:  # 避免访问父节点
                    dfs(y, x, depth + 1)  # x 是 y 的父节点
                    size[x] += size[y]  # 累加 x 的儿子 y 的子树大小
        dfs(0, -1, 0)  # 0 没有父节点

        # 只需要考虑 节点 x 和 y 的相对关系即可
        def reroot(x: int, fa: int) -> None:
            for y in g[x]:  # 遍历 x 的邻居 y
                if y != fa:  # 避免访问父节点
                    self.result[y] = self.result[x] + n - 2 * size[y] 
                    reroot(y, x)  # x 是 y 的父节点
        reroot(0, -1)  # 0 没有父节点
        
    def get_result(self) -> List[int]:
        return self.result