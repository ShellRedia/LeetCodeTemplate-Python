class KMP:
    def __init__(self, pattern:str):
        self.pattern = pattern
        self.match = [0] * len(pattern)
        c = 0
        for i in range(1, len(pattern)):
            v = pattern[i]
            while c and pattern[c] != v: c = self.match[c - 1]
            if pattern[c] == v: c += 1
            self.match[i] = c
    
    # 返回 text 中出现了多少次 pattern（允许 pattern 重叠）
    def search(self, text:str)->int:
        match_cnt = c = 0
        for i, v in enumerate(text):
            v = text[i]
            while c and self.pattern[c] != v: c = self.match[c - 1]
            if self.pattern[c] == v: c += 1
            if c == len(self.pattern):
                match_cnt += 1
                c = self.match[c - 1]
        return match_cnt