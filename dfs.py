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

# 二叉树遍历，前序遍历，lv: 层数(level, 从0开始); cd: 编号(code, 兄弟节点，右节点比左节点+1)
# 看着很长，但是包括了左右节点和父节点的相互关系，以及自己有多少的子节点，因此考虑了各种情况下，能够尽可能节省时间
lv_dct, cd_dct = {}, {}
left_s, right_s = set(), set()
fa_dct, left_bro, right_bro = defaultdict(), defaultdict(), defaultdict()
vals = []
cnts = Counter()
def f(o, lv, cd, fa):
    cnt = 0
    if not o:
        return cnt

    fa_dct[o] = fa
    lv_dct[o] = lv
    cd_dct[cd] = o
    vals.append(o.val)
    if o.left and o.right:
        cnt += f(o.left, lv + 1, cd * 2, o)
        cnt += f(o.right, lv + 1, cd * 2 + 1, o)
        left_s.add(o.left)
        right_s.add(o.right)
        left_bro[o.right] = o.left
        right_bro[o.left] = o.right

    elif o.left and not o.right:
        cnt += f(o.left, lv + 1, cd * 2, o)
        left_s.add(o.left)
    elif not o.left and o.right:
        cnt += f(o.right, lv + 1, cd * 2 + 1, o)
        right_s.add(o.right)
    else:
        pass
    cnts[o] = cnt
    return cnt

f(root, 0, 1, None)

# 数位DP:
'''
mask: 是否选过; 
isLimit: 表示当前是否受到了 n 的约束(注意要构造的数字不能超过 n);
isNum: 表示 i 前面的数位是否填了数字;
cnt: 数位之和，也可表示其他约束条件，需要自行改造。
'''

def digit_dp(s):
    @cache
    def f(i: int, mask: int, is_limit: bool, is_num: bool, cnt) -> int:
        if i == len(s):
            flag = (cnt > 0) # 比如还有一个约束条件，数位和大于 0
            return int(is_num and flag)  # is_num 为 True 表示得到了一个合法数字
        res = 0
        if not is_num:  # 可以跳过当前数位
            res = f(i + 1, mask, False, False, cnt)
        low = 0 if is_num else 1  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
        up = int(s[i]) if is_limit else 9  # 如果前面填的数字都和 n 的一样，那么这一位至多填 s[i]（否则就超过 n 啦）
        for d in range(low, up + 1):  # 枚举要填入的数字 d
            # 如果不能重复选:
            if (mask >> d & 1) == 0:  # d 不在 mask 中
                res += f(i + 1, mask | (1 << d), is_limit and d == up, True, cnt + d) # 统计一共有多少个 1: ... True ,cnt + int(d == 1))
            # 如果可以重复选:
            # res += f(i + 1, mask, is_limit and d == up, True, cnt + d)
        return res
    return f(0, 0, True, False, 0)
num = 114514
digit_dp(str(num))