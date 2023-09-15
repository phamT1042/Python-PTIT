class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def calC(A, B):
        C = SoPhuc(0, 0)
        C.thuc, C.ao = A.thuc + B.thuc, A.ao + B.ao
        C.thuc, C.ao = C.thuc * A.thuc - C.ao * A.ao, A.thuc * C.ao + C.thuc * A.ao
        return C
    
    def calD(A, B):
        D = SoPhuc(0, 0)
        D.thuc, D.ao = A.thuc + B.thuc, A.ao + B.ao
        D.thuc, D.ao = D.thuc * D.thuc - D.ao * D.ao, D.thuc * D.ao + D.thuc * D.ao
        return D

    def __str__(self):
        return ("%d + %di" % (self.thuc, self.ao)) if self.ao > 0 else ("%d - %di" % (self.thuc, -self.ao))

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        aThuc, aAo, bThuc, bAo = map(int, input().split())
        A = SoPhuc(aThuc, aAo)
        B = SoPhuc(bThuc, bAo)
        print("%s, %s" % (SoPhuc.calC(A, B), SoPhuc.calD(A, B)))