from functools import *

class EditDist:
    def __init__(self, word1, word2):
        m, n = len(word1), len(word2)
        @cache
        def f(i, j):
            if i == m: return n-j
            if j == n: return m-i
            if word1[i] == word2[j]: return f(i+1, j+1)
            return min(f(i+1, j), f(i, j+1), f(i+1, j+1)) + 1
        self.dist = f(0, 0)

    def get_edit_dist(self):
        return self.dist

# if __name__=="__main__":
#     ed = EditDist(word1, word2)
#     ed.get_edit_dist()