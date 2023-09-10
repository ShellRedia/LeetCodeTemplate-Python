# 二维差分:快速地把一个矩形范围内的数都 + x
class Difference2D:
    def __int__(self, m, n, rects):
        diff = [[0] * (m + 2) for _ in range(n + 2)]
        for r1, r2, c1, c2, x in rects:
            # 将区域 r1<=r<=r2 && c1<=c<=c2 上的数都加上 x
            # 多 +1 是为了方便求后面用二维前缀和复原
            diff[r1 + 1][c1 + 1] += x
            diff[r1 + 1][c2 + 2] -= x
            diff[r2 + 2][c1 + 1] -= x
            diff[r2 + 2][c2 + 2] += x
        # 根据差分矩阵复原 (二维前缀和)，得到矩阵的真实值:
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]
        self.mat = diff

    def get_value(self, x, y):
        return self.mat[x][y]
