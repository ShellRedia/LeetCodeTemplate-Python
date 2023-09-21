# 抄的板子，其中需要修改的是 _do 和 _query 的规则，用于区间更新和区间查询
class LazySegmentTree:
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.nums = nums
        self.ones = [0] * (4 * self.n)
        self.lazy = [False] * (4 * self.n)
        self._build(0, 0, self.n - 1)

    def _build(self, o: int, l: int, r: int) -> None:
        if l == r:
            self.ones[o] = self.nums[l]
            return
        left, right = 2 * o + 1, 2 * o + 2
        mid = (l + r) // 2
        self._build(left, l, mid)
        self._build(right, mid + 1, r)
        self.ones[o] = self.ones[left] + self.ones[right]

    def _do(self, o: int, l: int, r: int, val) -> None:
        self.ones[o] = (r - l + 1)  - self.ones[o]
        self.lazy[o] = not self.lazy[o]

    def _pushdown(self, o: int, l: int, r: int) -> None:
        if self.lazy[o]:
            left, right = 2 * o + 1, 2 * o + 2
            mid = (l + r) // 2
            self._do(left, l, mid, 0)
            self._do(right, mid + 1, r, 0)
            self.lazy[o] = False

    def _update(self, o: int, l: int, r: int, ql: int, qr: int, val) -> None:
        if ql <= l and r <= qr:
            self._do(o, l, r, val)
            return
        self._pushdown(o, l, r)
        left, right = 2 * o + 1, 2 * o + 2
        mid = (l + r) // 2
        if ql <= mid: self._update(left, l, mid, ql, qr, val)
        if mid + 1 <= qr: self._update(right, mid + 1, r, ql, qr, val)
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

    def update(self, ql: int, qr: int, val:int) -> None:
        self._update(0, 0, self.n - 1, ql, qr, val)

    def query(self, ql: int, qr: int) -> int:
        return self._query(0, 0, self.n - 1, ql, qr)

# segment_tree = LazySegmentTree(nums=nums)