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
            if x not in cur.children.keys():
                cur.children[x] = TrieNode()
            cur = cur.children[x]
            cur.cnt += 1

    def search_count(self, arr) -> int:
        cur = self.head
        rnt = 0
        for x in arr:
            if x not in cur.children.keys():
                return 0
            cur = cur.children[x]
            rnt = cur.cnt
        for x in cur.children.values():
            rnt -= x.cnt
        return rnt

    def pre_count(self, prefix) -> int:
        cur = self.head
        rnt = 0
        for x in prefix:
            if x not in cur.children.keys():
                return 0
            cur = cur.children[x]
            rnt = cur.cnt
        return rnt
trie = Trie()


