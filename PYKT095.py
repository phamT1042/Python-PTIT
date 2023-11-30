class KH:
    __cnt = 1
    def __init__(self, name, loai, chiSoDau, chiSoCuoi):
        self.__maKH = "KH{:02d}".format(KH.__cnt)
        KH.__cnt += 1

        chars = name.split()
        self.__name = ""
        for i in chars: self.__name += i.title() + " "
        self.__name = self.__name.rstrip()
        self.__trongDinhMuc = self.__vuotDinhMuc = self.__VAT = 0

        if loai == 'A': dinhMuc = 100
        elif loai == 'C': dinhMuc = 200
        else: dinhMuc = 500

        diff = chiSoCuoi - chiSoDau
        if diff > dinhMuc:
            self.__trongDinhMuc = 450 * dinhMuc
            self.__vuotDinhMuc = (diff - dinhMuc) * 1000
            self.__VAT = self.__vuotDinhMuc * 5 // 100
        else:
            self.__trongDinhMuc = diff * 450

        self.__phaiTra = self.__trongDinhMuc + self.__vuotDinhMuc + self.__VAT

    def __lt__(self, other):
        return self.__phaiTra > other.__phaiTra

    def __str__(self):
        return self.__maKH + " " + self.__name + " " + str(self.__trongDinhMuc) + " " + \
    str(self.__vuotDinhMuc) + " " + str(self.__VAT) + " " + str(self.__phaiTra)
    
n = int(input())
listKH = []
for i in range(n):
    name = input()
    data = input().split()
    listKH.append(KH(name, data[0], int(data[1]), int(data[2])))

listKH.sort()
for i in range(n):
    print(listKH[i])