from collections import *
'''
处理联通分量的问题：
给每个联通分量一个都赋值一个id
注意，该方法相对耗时，有TLE的风险
'''
class ConnectedComponent:
    def __init__(self, grid, directions=4, cal_adjacent=False):
        directs = []
        if directions == 4: directs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        elif directions == 8: directs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        m, n = len(grid), len(grid[0])
        vis = set()
        self.components, self.adjacency = defaultdict(list), defaultdict(set)
        self.val2ids, self.id2val = defaultdict(list), {}
        self.pixel2id = {}
        id = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in vis:
                    dq = deque([(i, j)])
                    vis.add((i, j))
                    self.components[id].append((i, j))
                    self.pixel2id[(i, j)] = id
                    self.val2ids[grid[i][j]].append(id)
                    self.id2val[id] = grid[i][j]
                    while dq:
                        x, y = dq.popleft()
                        for dx, dy in directs:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in vis:
                                if grid[nx][ny] == grid[i][j]:
                                    dq.append((nx, ny))
                                    vis.add((nx, ny))
                                    self.components[id].append((nx, ny))
                                    self.pixel2id[(nx, ny)] = id
                    id += 1
        if cal_adjacent:
            for x in range(m):
                for y in range(n):
                    for dx, dy in directs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != grid[x][y]:
                            self.adjacency[self.pixel2id[(x, y)]].add(self.pixel2id[(nx, ny)])

    def get_ids_by_value(self, val: int) -> list:
        return self.val2ids[val]

    def get_value_by_id(self, id: int) -> int:
        return self.id2val[id]

    def get_component_by_id(self, id: int) -> list:
        return self.components[id]

    def get_components_count(self) -> int:
        return len(self.components)

    def get_adjacent_ids(self, id: int) -> set:
        return self.adjacency[id]

    def is_adjacent_by_id(self, x, y) -> list:
        return x in self.adjacency[y]

    def get_all_values(self) -> list:
        return sorted(self.val2comp_ids.keys())