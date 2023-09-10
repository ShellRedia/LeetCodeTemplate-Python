# 滚动哈希，e.g.：1044. 最长重复子串, 两套进制
# 高位 -> 低位
class RollingHash:
    def __init__(self, s, base1=31, base2=71):
        n = len(s)  # s 要处理的字符串
        self.MOD = 10 ** 18 + 7 # 是必要的，否则计算速度超级慢
        # encoder：获取字母在字母表中的顺序:
        ecd = {chr(i + ord('a')): i for i in range(26)}
        hvs1, hvs2 = [0] * (n + 1), [0] * (n + 1)
        pow1, pow2 = [1] * (n + 1), [1] * (n + 1)
        for i in range(n):
            hvs1[i + 1] = (hvs1[i] * base1 + ecd[s[i]]) % self.MOD
            hvs2[i + 1] = (hvs2[i] * base2 + ecd[s[i]]) % self.MOD
            pow1[i + 1] = (pow1[i] * base1) % self.MOD
            pow2[i + 1] = (pow2[i] * base2) % self.MOD
        self.hvs1, self.hvs2 = hvs1, hvs2
        self.pow1, self.pow2 = pow1, pow2

    # 获取子串s[start:end)哈希值，元组形式返回:
    def get_hash(self, start, end):
        hash_1 = (self.hvs1[end] - self.hvs1[start] * self.pow1[end - start]) % self.MOD
        hash_2 = (self.hvs2[end] - self.hvs2[start] * self.pow2[end - start]) % self.MOD
        return (hash_1, hash_2)
