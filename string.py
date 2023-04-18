#滚动哈希：
# 字符串编码函数
def ecd(ch):
    return ord(ch) - ord('a') + 1

mod = 10**9+7
base = 31       # s仅包含小写字母，base可取31

n = len(s)
# 预处理出前缀字符串的哈希值 和 base进制的幂
prefix = [0] * (n+1)    # prefix[i]: 字符串s[0:i]的哈希值
mul = [1] * (n+1)       # mul[i]: base ** i
for i in range(1, n+1):
    prefix[i] = ( prefix[i-1] * base + ecd(s[i-1]) ) % mod
    mul[i] = mul[i-1] * base % mod
