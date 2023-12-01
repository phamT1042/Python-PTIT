class TienNuoc:
    __cnt = 1
    def __init__(self, ten, chiSoDau, chiSoCuoi):
        self.__ma = 'KH{:02d}'.format(TienNuoc.__cnt)
        TienNuoc.__cnt += 1
        self.__ten = ten
        self.__chiSoDau = chiSoDau
        self.__chiSoCuoi = chiSoCuoi

        diff = self.__chiSoCuoi - self.__chiSoDau
        self.__tien = 0
        if diff > 50:
            self.__tien = 100 * 50
            if diff > 100:
                self.__tien += 150 * 50 + 200 * (diff - 100)
                self.__tien *= 105 / 100
            else:
                self.__tien += 150 * (diff - 50)
                self.__tien *= 103 / 100
        else:
            self.__tien = 102 * diff 

    def __str__(self):
        return self.__ma + " " + self.__ten + " " + str(round(self.__tien))

    def __lt__(self, other):
        return self.__tien > other.__tien
    

n = int(input())
listKH = []
for _ in range(n):
    listKH.append(TienNuoc(input(), int(input()), int(input())))

listKH.sort()
print(*listKH, sep = '\n')

