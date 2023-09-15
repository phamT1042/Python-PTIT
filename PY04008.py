import sys
def stdin_gen():
    for x in sys.stdin.read().split():
        yield int(x)
cin = stdin_gen()

class Matrix:
    def __init__(self, n, m, mt):
        self.n = n
        self.m = m
        self.mt = mt
    
    def mulMatrix(self):
        res = Matrix(self.n, self.n, [[0] * self.n for _ in range(self.n)])
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.m):
                    res.mt[i][j] += self.mt[i][k] * self.mt[j][k]
        return res
    
    def out(self):
        for i in self.mt: print(*i)

if __name__ == '__main__':
    t = next(cin)
    while t > 0:
        t -= 1
        n, m = next(cin), next(cin)
        a = []
        for _ in range(n): 
            tmp = []
            for i in range(m):
                tmp.append(next(cin))
            a.append(tmp)
        Matrix(n, m, a).mulMatrix().out()