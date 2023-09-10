# 滚动哈希，e.g.：1044. 最长重复子串, 单进制
# 高位 -> 低位
class RollingHash:
    def __init__(self, s, base=71):
        n = len(s)  # s 要处理的字符串
        self.MOD = 10 ** 18 + 7 # 是必要的，否则计算速度超级慢
        # encoder：获取字母在字母表中的顺序:
        ecd = {chr(i + ord('a')): i for i in range(26)}
        self.hvs, self.pow = [0] * (n + 1), [1] * (n + 1)
        for i in range(n):
            self.hvs[i + 1] = (self.hvs[i] * base + ecd[s[i]]) % self.MOD
            self.pow[i + 1] = (self.pow[i] * base) % self.MOD

    # 获取子串s[start:end)哈希值，元组形式返回:
    def get_hash(self, start, end):
        return (self.hvs[end] - self.hvs[start] * self.pow[end - start]) % self.MOD
