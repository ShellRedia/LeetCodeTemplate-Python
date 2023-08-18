'''
因为dfs这一技巧对于不同的问题有自己的形式，
实在是难以找到一个统一的模板，所以专门开一个文件来讨论记录，
或是等到我实力有所增强后再做优化考虑。
'''


# 选词填空
'''
这是最近才遇到的问题(2023年5月3日)，大致意思是有一个串里面有若干空，每个空有若干个候选项，问有多少种填空方式，自己写也不难，但是总感觉花时间。
形式：AB[CDE]FG[HI] -> [ABCFGH, ABCFGI, ABDFGH, ABDFGI, ABEFGH, ABEFGI]
'''
template = ["A", "B", "_", "F", "G", "_"] # 模板串
fill_positions = [2, 5] # 要填写选项位置
options = [["C", "D", "E"], ["H", "I"]] # 可供填写的选项（离散化处理）
get_fill_pos = {x:i for i, x in enumerate(fill_positions)} # 解离散化
rt, perm = [], [] # 临时变量：rt: 表示当前正在搜索的路径，perm: 存放所有符合条件的路径
def permutation_options(idx): # 参数：idx: 当前正在填写的索引
    if idx == len(template):
        perm.append(rt.copy())
        return 
    if idx in get_fill_pos.keys():
        for x in options[get_fill_pos[idx]]:
            rt.append(x)
            permutation_options(idx+1)
            rt.pop()
    else:
        rt.append(template[idx])
        permutation_options(idx+1)
        rt.pop()
permutation_options(0)
result = perm

# 数位DP:
'''
mask: 是否选过; 
isLimit: 表示当前是否受到了 n 的约束(注意要构造的数字不能超过 n);
isNum: 表示 i 前面的数位是否填了数字;
x: 当前状态，也可表示其他约束条件，需要自行改造。
'''

class DigitDP:
    def __init__(self, is_mod=True, repeat=False, leading_zero=False, iter_cond=lambda x, y: True, iter_op=lambda x, y: x, return_cond=lambda x: x > 0):
        self.MOD = 10 ** 9 + 7 if is_mod else 1 # 是否取模
        self.repeat = repeat # 是否允许重复数字
        self.leading_zero = leading_zero # 是否允许前导0
        self.iter_cond = iter_cond # 递推约束条件
        self.iter_op = iter_op # 递推方式
        self.return_cond = return_cond # 计数约束条件
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
                res %= self.MOD
            return res
        return f(0, 0, True, self.leading_zero, 0)