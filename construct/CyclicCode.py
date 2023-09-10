# 循环码(返回二进制字符串列表，参数n为二进制长度):
def cyclic_code(n):
    if n <= 0: return []
    codes = ['0', '1']
    for i in range(n - 1): codes = [code + '0' for code in codes] + [code + '1' for code in reversed(codes)]
    return codes