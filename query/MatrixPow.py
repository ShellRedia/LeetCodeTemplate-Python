'''
k 个 同样的方阵相乘
'''
class MatrixPow:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
        self.MOD = 10 ** 9 + 7

    # 矩阵乘法
    def multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        c = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    c[i][j] += a[i][k] * b[k][j] 
                    #c[i][j] %= self.MOD
        return c

    # 矩阵快速幂
    def pow(self, k: int) -> List[List[int]]:
        res = [[0 for _ in range(self.n)] for _ in range(self.n)]
        a = self.matrix
        for i in range(self.n): res[i][i] = 1
        while k:
            if k % 2:
                res = self.multiply(res, a)
            a = self.multiply(a, a)
            k //= 2
        return res

# if __name__=="__main__":
#         m = [
#             [1, 1],
#             [1, 0]
#         ]
#         mp = MatrixPow(m)
#         m = mp.pow(k)
#         return m[0][1]