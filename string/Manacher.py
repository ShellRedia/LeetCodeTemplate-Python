
# 回文子串数量O(n)，待简化
def countSubstrings(s: str) -> int:
    def manacher():
        # 马拉车算法
        arm = [0] * n
        x, y = 0, -1
        for i in range(0, n):
            k = 1 if i > y else min(arm[x + y - i], y - i + 1)

            # 持续增加回文串的长度
            while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                k += 1
            arm[i] = k

            # 更新右侧最远的回文串边界
            k -= 1
            if i + k > y:
                x = i - k
                y = i + k
        # 返回每个位置往右的臂长
        return arm

    s = "#" + "#".join(list(s)) + "#"
    n = len(s)
    dp = manacher()

    # 计算真实长度回文串的个数
    ans = 0
    for num in dp:
        num = (num * 2 - 1) // 2
        if num % 2 == 0:
            ans += num // 2
        else:
            ans += num // 2 + 1
    return ans
