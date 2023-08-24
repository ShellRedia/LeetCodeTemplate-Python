# from collections import *
#
# # 二叉树问题
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class BinaryTree:
    def __init__(self, root: TreeNode):
        self._node2level = Counter()
        self._node2pos = Counter()
        self._subtree_counts = Counter()
        self._subtree_sum = Counter()
        self._pos2node = defaultdict(lambda: None)
        self._node2father = defaultdict(lambda: None)
        self._node2leftbro = defaultdict(lambda: None)
        self._node2rightbro = defaultdict(lambda: None)
        self._level2nodes = defaultdict(list)
        self._adjacency_lst = defaultdict(list)
        self._preorder, self._inorder, self._postorder = [], [], []
        self._leaves, self._leftnodes, self._rightnodes = set(), set(), set()
        self._height = 0

        def dfs(o, level, pos, father) -> tuple:
            if not o: return 0, 0
            subtree_cnt, subtree_sum = 1, o.val
            self._node2level[o] = level
            self._level2nodes[level].append(o)
            self._node2pos[o], self._pos2node[pos] = pos, o
            self._node2father[o] = father
            self._preorder.append(o)

            if father: self._adjacency_lst[o].append(father)

            if o.left and o.right:
                cnt, _sum = dfs(o.left, level + 1, pos * 2, o)
                subtree_cnt += cnt
                subtree_sum += _sum
                self._inorder.append(o)
                cnt, _sum = dfs(o.right, level + 1, pos * 2 + 1, o)
                subtree_cnt += cnt
                subtree_sum += _sum
                self._node2leftbro[o.right] = o.left
                self._node2rightbro[o.left] = o.right
                self._adjacency_lst[o].append(o.left)
                self._adjacency_lst[o].append(o.right)
            elif o.left and not o.right:
                cnt, _sum = dfs(o.left, level + 1, pos * 2, o)
                subtree_cnt += cnt
                subtree_sum += _sum
                self._leftnodes.add(o.left)
                self._inorder.append(o)
                self._adjacency_lst[o].append(o.left)
            elif not o.left and o.right:
                self._inorder.append(o)
                cnt, _sum = dfs(o.right, level + 1, pos * 2 + 1, o)
                subtree_cnt += cnt
                subtree_sum += _sum
                self._rightnodes.add(o.right)
                self._adjacency_lst[o].append(o.right)
            else:
                self._inorder.append(o)
                self._leaves.add(o)
            self._postorder.append(o)
            self._subtree_counts[o] = subtree_cnt
            self._subtree_sum[o] = subtree_sum
            self._height = max(self._height, level + 1)
            return subtree_cnt, subtree_sum

        dfs(root, 0, 0, None)

    def get_level(self, o: TreeNode) -> int: # 获取节点的层数 (从 0 开始)
        return self._node2level[o]

    def get_pos(self, o: TreeNode) -> int: # 获取节点的位置
        return self._node2pos[o]

    def get_node_by_pos(self, pos: int) -> TreeNode: # 通过位置获取节点
        return self._pos2node[pos]

    def get_father_node(self, o: TreeNode) -> TreeNode: # 获取父节点（如果有，否则为None）
        return self._node2father[o]

    def get_lca(self, p: TreeNode, q: TreeNode) -> TreeNode: # 获取该树中两个指定节点的最近公共祖先（如果有，否则为None）
        s = set()
        while p:
            s.add(p)
            p = self.get_father_node(p)
        while q:
            if q in s: return q
            q = self.get_father_node(q)
        return None

    def get_left_bro_node(self, o: TreeNode) -> TreeNode: # 获取左兄弟节点（如果有，否则为None）
        return self._node2leftbro[o]

    def get_right_bro_node(self, o: TreeNode) -> TreeNode: # 获取右兄弟节点（如果有，否则为None）
        return self._node2rightbro[o]

    def get_level_nodes(self, level: int) -> list[TreeNode]: # 获取指定层的所有节点
        return self._level2nodes[level]

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

    def get_height(self): # 获取树的高度
        return self._height