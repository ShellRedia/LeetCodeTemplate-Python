from collections import *
from bisect import *
from math import *

# 二叉树问题
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
--- 从此处复制 ---
'''
# 树上倍增 查询第 k 个祖先节点：leetcode 1483
class TreeDoubling:
    '''
    parents: 父节点关系的数组，parents[i] 是 i 的父节点
    k: 最大查询范围，可以很大（10**10）,反正会指数折叠
    '''
    def __init__(self, parents, k):
        self.m = k.bit_length()
        pa = {}
        for x, p in parents.items():
            pa[x] = [p] + [None] * self.m
        for i in range(self.m):
            for x in parents:
                if pa[x][i]: pa[x][i+1] = pa[pa[x][i]][i]
        self.pa = pa
    '''
    node: 要查询的节点
    k: 与节点x的距离
    '''
    def get_Kth_ancestor(self, node, k):
        for i in range(k.bit_length()):
            if (k >> i) & 1:
                node = self.pa[node][i]
                if node == None: return None # node 可能为 0
        return node

class BinaryTree:
    def __init__(self, root: TreeNode):
        self._node2depth = Counter()
        self._node2pos = Counter()
        self._subtree_counts = Counter()
        self._subtree_sum = Counter()
        self._pos2node = defaultdict(lambda: None)
        self._node2parent = defaultdict(lambda: None)
        self._node2leftbro = defaultdict(lambda: None)
        self._node2rightbro = defaultdict(lambda: None)
        self._depth2nodes = defaultdict(list)
        self._adjacency_lst = defaultdict(list)
        self._preorder, self._inorder, self._postorder = [], [], []
        self._leaves, self._leftnodes, self._rightnodes = [], [], []
        self._height = 0

        def dfs(o, depth, pos, parent) -> tuple:
            if not o: return 0, 0
            subtree_cnt, subtree_sum = 1, o.val
            self._node2depth[o] = depth
            self._depth2nodes[depth].append(o)
            self._node2pos[o], self._pos2node[pos] = pos, o
            self._node2parent[o] = parent
            self._preorder.append(o)

            if parent: self._adjacency_lst[o].append(parent)

            if o.left and o.right:
                cnt, _sum = dfs(o.left, depth + 1, pos * 2, o)
                subtree_cnt += cnt
                subtree_sum += _sum
                self._inorder.append(o)
                cnt, _sum = dfs(o.right, depth + 1, pos * 2 + 1, o)
                subtree_cnt += cnt
                subtree_sum += _sum
                self._node2leftbro[o.right] = o.left
                self._node2rightbro[o.left] = o.right
                self._adjacency_lst[o].append(o.left)
                self._adjacency_lst[o].append(o.right)
            elif o.left and not o.right:
                cnt, _sum = dfs(o.left, depth + 1, pos * 2, o)
                subtree_cnt += cnt
                subtree_sum += _sum
                self._leftnodes.append(o.left)
                self._inorder.append(o)
                self._adjacency_lst[o].append(o.left)
            elif not o.left and o.right:
                self._inorder.append(o)
                cnt, _sum = dfs(o.right, depth + 1, pos * 2 + 1, o)
                subtree_cnt += cnt
                subtree_sum += _sum
                self._rightnodes.append(o.right)
                self._adjacency_lst[o].append(o.right)
            else:
                self._inorder.append(o)
                self._leaves.append(o)
            self._postorder.append(o)
            self._subtree_counts[o] = subtree_cnt
            self._subtree_sum[o] = subtree_sum
            self._height = max(self._height, depth + 1)
            return subtree_cnt, subtree_sum

        dfs(root, 0, 0, None)
        self.td = TreeDoubling(self._node2parent, self._height)
        self._node2depth[None] = -1
        self._node2pos[None] = -1
        self._subtree_counts[None] = -1
        self._subtree_sum[None] = -1

    def get_node_depth(self, o: TreeNode) -> int: # 获取节点的深度 (从 0 开始)
        return self._node2depth[o]

    def get_pos(self, o: TreeNode) -> int: # 获取节点的位置
        return self._node2pos[o]

    def get_node_by_pos(self, pos: int) -> TreeNode: # 通过位置获取节点
        return self._pos2node[pos]

    def get_parent_node(self, o: TreeNode) -> TreeNode: # 获取父节点（如果有，否则为None）
        return self._node2parent[o]

    def get_lca(self, nodes: list[TreeNode]) -> TreeNode: # 获取该树中两个指定节点的最近公共祖先（log(height) 如果有，否则为None）
        if not nodes: return None
        depths = [self.get_node_depth(x) for x in nodes]
        mn_depth = min(depths)
        nodes = [self.td.get_Kth_ancestor(x, d-mn_depth) for x, d in zip(nodes, depths)]
        def check(lmt):
            return len(set(self.td.get_Kth_ancestor(x, lmt) for x in nodes)) == 1
        k = bisect_left(range(mn_depth), True, key=check)
        return self.td.get_Kth_ancestor(nodes[0], k)

    def get_dist(self, p: TreeNode, q: TreeNode) -> int:
        x = self.get_lca([p, q])
        return self.get_node_depth(p) + self.get_node_depth(q) - 2 * self.get_node_depth(x)

    def get_left_bro_node(self, o: TreeNode) -> TreeNode: # 获取左兄弟节点（如果有，否则为None）
        return self._node2leftbro[o]

    def get_right_bro_node(self, o: TreeNode) -> TreeNode: # 获取右兄弟节点（如果有，否则为None）
        return self._node2rightbro[o]

    def get_depth_nodes(self, depth: int) -> list[TreeNode]: # 获取指定层的所有节点
        return self._depth2nodes[depth]

    def get_adjacency_nodes(self, o: TreeNode) -> list[TreeNode]: # 获取所有邻接节点
        return self._adjacency_lst[o]

    def get_preorder(self) -> list[TreeNode]: # 获取前序遍历
        return self._preorder

    def get_inorder(self) -> list[TreeNode]: # 获取中序遍历
        return self._inorder

    def get_postorder(self) -> list[TreeNode]: # 获取后序遍历
        return self._postorder

    def get_leaves(self) -> set: # 获取所有叶节点
        return self._leaves

    def get_left_nodes(self) -> set: # 获取所有左节点
        return self._leftnodes

    def get_right_nodes(self) -> set: # 获取所有右节点
        return self._rightnodes

    def get_subtree_count(self, o: TreeNode) -> int: # 获取子节点的数量
        return self._subtree_counts[o]

    def get_subtree_sum(self, o: TreeNode) -> int: # 获取子节点的值总和
        return self._subtree_sum[o]

    def get_height(self) -> int: # 获取树的高度
        return self._height
