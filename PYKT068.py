class MH:
    def __init__(self, ma, ten, thi):
        self.__ma = ma
        self.__ten = ten
        self.__thi = thi
    
    def __lt__(self, other):
        return self.__ma < other.__ma
    
    def __str__(self):
        return self.__ma + " " + self.__ten + " " + self.__thi

n = int(input())
listMH = []
for i in range(n):
    listMH.append(MH(input(), input(), input()))
listMH.sort()
print(*listMH, sep = '\n')