from functools import *
'''
mask: 是否选过;
isLimit: 表示当前是否受到了 n 的约束(注意要构造的数字不能超过 n);
isNum: 表示 i 前面的数位是否填了数字;
x: 当前状态，也可表示其他约束条件，需要自行改造。
'''
class DigitDP:
    def __init__(self):
        self.is_mod = True
        self.MOD = 10 ** 9 + 7
        self.repeat = False # 是否允许重复数字
        self.leading_zero = False # 是否允许前导0
        self.iter_cond = lambda x, y: True # 递推约束条件
        self.iter_op = lambda x, y: x # 递推方式
        self.return_cond = lambda x: x > 0 # 计数约束条件

    def get_count(self, s):
        @cache
        def f(i: int, mask: int, is_limit: bool, is_num: bool, x: int) -> int:
            if i == len(s): return int(is_num and self.return_cond(x))
            res = 0
            if not is_num: res = f(i + 1, mask, False, False, x)
            low = 0 if is_num else 1
            up = int(s[i]) if is_limit else 9
            for d in range(low, up + 1):
                if self.repeat:
                    if self.iter_cond(d, x):
                        res += f(i + 1, mask, is_limit and d == up, True, self.iter_op(d, x))
                else:
                    if self.iter_cond(d, x) and (mask >> d & 1) == 0:
                        res += f(i + 1, mask | (1 << d), is_limit and d == up, True, self.iter_op(d, x))
                if self.is_mod: res %= self.MOD
            return res
        return f(0, 0, True, self.leading_zero, 0)

# digit_dp = DigitDP()
# cnt = digit_dp.get_count(s) # s: str, 范围: (0, int(s)]