save = dict()
for _ in range(int(input())):
    s = input()
    save[s[:2]] = s[3:]

class NhanVien:
    def __init__(self, ma, ten, luongCB, soNgayCong):
        self.__ma = ma
        self.__ten = ten
        self.__luongCB = luongCB
        self.__soNgayCong = soNgayCong
        self.__phongBan = save[ma[3:]]
        self.__luongThang = luongCB * soNgayCong
        nhom, nam = ma[0], int(ma[1:3])
        if nam >= 1 and nam <= 3:
            if nhom == 'A' or nhom == 'B': self.__luongThang *= 10
            elif nhom == 'C': self.__luongThang *= 9
            else: self.__luongThang *= 8
        elif nam >= 4 and nam <= 8:
            if nhom == 'A': self.__luongThang *= 12
            elif nhom == 'B': self.__luongThang *= 11
            elif nhom == 'C': self.__luongThang *= 10
            else: self.__luongThang *= 9
        elif nam >= 9 and nam <= 15:
            if nhom == 'A': self.__luongThang *= 14
            elif nhom == 'B': self.__luongThang *= 13
            elif nhom == 'C': self.__luongThang *= 12
            else: self.__luongThang *= 11
        else:
            if nhom == 'A': self.__luongThang *= 20
            elif nhom == 'B': self.__luongThang *= 16
            elif nhom == 'C': self.__luongThang *= 14
            else: self.__luongThang *= 13

    def __str__(self):
        return self.__ma + " " + self.__ten + " " + self.__phongBan + " " + str(self.__luongThang * 1000)

res = []
for _ in range(int(input())):
    res.append(NhanVien(input(), input(), int(input()), int(input())))

for x in res: print(x)