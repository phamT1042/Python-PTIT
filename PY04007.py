
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
    t = int(input())
    while t > 0:
        t -= 1
        n, m = map(int, input().split())
        a = []
        for _ in range(n): 
            a.append(list(map(int, input().split())))
        Matrix(n, m, a).mulMatrix().out()