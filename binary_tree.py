from collections import *

# 二叉树遍历
# 看着很长，但考虑了各种情况下的，能够尽可能节省时间
node2level = Counter() # 节点(node)->节点所在层数(int)
level2nodes = defaultdict(list) # 层数(int)->所包含的节点(node)

node2code = Counter() # 节点(node)->节点编号(int)
code2node = defaultdict() # 节点编号(int)->节点(node)

node2father, node2leftbro, node2rightbro = defaultdict(), defaultdict(), defaultdict() # 节点(node)->父节点，左兄弟节点，右兄弟节点(node)
leftnodes, rightnodes, leaves = set(), set(), set() # 左节点，右节点，叶子节点的集合
preorder, inorder, postorder = [], [], [] # 前序，中序，后序遍历
children_counts = Counter() #当前节点的子节点个数

def f(o, level, code, father):
    children_cnt = 0
    if not o:
        return children_cnt
    node2level[o] = level
    level2nodes[level].append(o)
    node2code[o] = code
    code2node[code] = o
    node2father[o] = father
    preorder.append(o)

    if o.left and o.right:
        children_cnt += f(o.left, level + 1, code * 2, o)
        inorder.append(o)
        children_cnt += f(o.right, level + 1, code * 2 + 1, o)
        node2leftbro[o.right] = o.left
        node2rightbro[o.left] = o.right
    elif o.left and not o.right:
        children_cnt += f(o.left, level + 1, code * 2, o)
        leftnodes.add(o.left)
        inorder.append(o)
    elif not o.left and o.right:
        inorder.append(o)
        children_cnt += f(o.right, level + 1, code * 2 + 1, o)
        rightnodes.add(o.right)
    else:
        leaves.add(o)
    postorder.add(o)
    children_counts[o] = children_cnt
    return children_cnt + 1

f(root, 0, 1, None)