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
lv_dct, cd_dct = {}, {}
left_s, right_s = set(), set()
fa_dct, left_bro, right_bro = defaultdict(), defaultdict(), defaultdict()

def f(o, lv, cd, fa):
    if not o:
        return
    fa_dct[o] = fa
    lv_dct[o] = lv
    cd_dct[cd] = o
    if o.left and o.right:
        f(o.left, lv + 1, cd * 2, o)
        f(o.right, lv + 1, cd * 2 + 1, o)
        left_s.add(o.left)
        right_s.add(o.right)
        left_bro[o.right] = o.left
        right_bro[o.left] = o.right

    elif o.left and not o.right:
        f(o.left, lv + 1, cd * 2, o)
        left_s.add(o.left)
    elif not o.left and o.right:
        f(o.right, lv + 1, cd * 2 + 1, o)
        right_s.add(o.right)
    else:
        pass

f(root, 0, 1, None)
