#滚动哈希，例题：1044. 最长重复子串。
n = len(s) # s 要处理的字符串
MOD = 10**9 + 7
base1, base2 = 31, 71   # 双哈希：两套进制
# encoder：获取字母在字母表中的顺序: 
ecd = {chr(i+ ord('a')):i for i in range(26)}     
hvs1, hvs2 = [0] * (n+1), [0] * (n+1)
pow1, pow2 = [1] * (n+1), [1] * (n+1)
for i in range(n):
    hvs1[i+1] = (hvs1[i] * base1 + ecd[s[i]]) % MOD
    hvs2[i+1] = (hvs2[i] * base2 + ecd[s[i]]) % MOD
    pow1[i+1] = (pow1[i] * base1) % MOD
    pow2[i+1] = (pow2[i] * base2) % MOD
# 获取子串s[start:end]哈希值，元组形式返回:
def get_hash(start, end):
    hash_1 = (hvs1[end] - hvs1[start] * pow1[end-start]) % MOD
    hash_2 = (hvs2[end] - hvs2[start] * pow2[end-start]) % MOD
    return (hash_1, hash_2)
