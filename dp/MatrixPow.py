'''
k 个 同样的方阵相乘
'''
class MatrixPow:
    def __init__(self, matrix, is_mod=False):
        self.matrix = matrix
        self.n = len(matrix)
        self.MOD = 10 ** 9 + 7
        self.is_mod = is_mod

    # 矩阵乘法
    def multiply(self, a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        c = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    c[i][j] += a[i][k] * b[k][j] 
                    if self.is_mod: c[i][j] %= self.MOD
        return c

    # 矩阵快速幂
    def pow(self, k: int) -> list[list[int]]:
        res = [[0 for _ in range(self.n)] for _ in range(self.n)]
        a = self.matrix
        for i in range(self.n): res[i][i] = 1
        while k:
            if k % 2:
                res = self.multiply(res, a)
            a = self.multiply(a, a)
            k //= 2
        return res

# mat = [
#     [1, 1],
#     [1, 0]
# ]
# matrix_pow = MatrixPow(mat)
# mat = matrix_pow.pow(k=k)