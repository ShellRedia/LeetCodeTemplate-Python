class BaseConvert:
    # 将 10 进制数字转换为任意的 k 进制字符串, 2 <= k < 10:
    def digit2k(self, num: int, k: int) -> str:
        if num == 0: return '0'
        flag = '-' if num < 0 else ''
        num = abs(num)
        result = ''
        while num > 0:
            num, remainder = divmod(num, k)
            result = str(remainder) + result
        return flag + result

    # 将 ka 进制字符串 转换为任意的 kb 进制字符串:
    def ka2kb(self, a: str, ka: int, kb: int) -> str:
        return self.digit2k(int(a, ka), kb)
