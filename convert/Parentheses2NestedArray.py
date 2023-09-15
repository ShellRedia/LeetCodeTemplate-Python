'''
将包含括号的字符串转换为嵌套的多维数组，以便后续处理
'''
def Parentheses2NestedArray(s: str, left_mark="(", right_mark=")")->list[str]:
    if not s: return []
    def f(left, right):
        if s.find(left_mark, left, right) == -1: return [s[left:right]]
        l = s.find(left_mark, left, right)
        r = s.rfind(right_mark, left, right)
        rnt, last, cnt = [], l, 0
        if s[left:l]: rnt.append(s[left:l])
        for i in range(l, r+1):
            if s[i] == left_mark: cnt += 1
            elif s[i] == right_mark: cnt -= 1
            if cnt == 0:
                t, last = f(last+1, i), i+1
                if t: rnt.append(t)
        if s[r+1:right]: rnt.append(s[r+1:right])
        return rnt
    return f(0, len(s))