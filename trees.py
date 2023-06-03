# 前缀树, 注意要灵活修改，否则也可能超时:
# insert: 插入一个串; search_count: 指定串出现的次数; pre_count: 指定前缀出现的次数
class TrieNode:
    def __init__(self):
        self.cnt = 0
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, arr) -> None:
        cur = self.head
        for x in arr:
            if not cur.children[x]:
                cur.children[x] = TrieNode(x)
            cur = cur.children[x]
            cur.cnt += 1

    def search_count(self, arr) -> int:
        cur = self.head
        rnt = 0
        for x in arr:
            if not cur.children[x]:
                return False
            cur = cur.children[x]
            rnt = cur.cnt
        for x in cur.children.values():
            rnt -= x.cnt
        return rnt

    def pre_count(self, prefix) -> int:
        cur = self.head
        rnt = 0
        for x in prefix:
            if not cur.children[x]:
                return 0
            cur = cur.children[x]
            rnt = cur.cnt
        return rnt
trie = Trie()

# 抄的板子，初始索引为0， 查询修改的区间范围为[L, R]的闭区间
class LazySegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.ones = [0] * (4 * self.n)
        self.lazy = [False] * (4 * self.n)
        self._build(0, 0, self.n-1)

    def _build(self, o: int, l: int, r: int) -> None:
        if l == r:
            self.ones[o] = self.nums[l]
            return
        left, right = 2 * o + 1, 2 * o + 2
        mid = (l + r) // 2
        self._build(left, l, mid)
        self._build(right, mid + 1, r)
        self.ones[o] = self.ones[left] + self.ones[right]

    def _do(self, o: int, l: int, r: int) -> None:
        self.ones[o] = r - l + 1 - self.ones[o]
        self.lazy[o] = not self.lazy[o]
            
    def _pushdown(self, o: int, l: int, r: int) -> None:
        if self.lazy[o]:
            left, right = 2 * o + 1, 2 * o + 2
            mid = (l + r) // 2
            self._do(left, l, mid)
            self._do(right, mid + 1, r)
            self.lazy[o] = False

    def _update(self, o: int, l: int, r: int, ql: int, qr: int) -> None:
        if ql <= l and r <= qr:
            self._do(o, l, r)
            return
        self._pushdown(o, l, r)
        left, right = 2 * o + 1, 2 * o + 2
        mid = (l + r) // 2
        if ql <= mid: self._update(left, l, mid, ql, qr)
        if mid + 1 <= qr: self._update(right, mid + 1, r, ql, qr)
        self.ones[o] = self.ones[left] + self.ones[right]

    def _query(self, o: int, l: int, r: int, ql: int, qr: int) -> int:
        if ql <= l and r <= qr:
            return self.ones[o]
        left, right = 2 * o + 1, 2 * o + 2
        mid = (l + r) // 2
        self._pushdown(o, l, r)
        ans = 0
        if ql <= mid: ans += self._query(left, l, mid, ql, qr)
        if mid + 1 <= qr: ans += self._query(right, mid + 1, r, ql, qr)
        return ans

    def update(self, ql: int, qr: int) -> None:
        self._update(0, 0, self.n-1, ql, qr)

    def query(self, ql: int, qr: int) -> int:
        return self._query(0, 0, self.n-1, ql, qr)
