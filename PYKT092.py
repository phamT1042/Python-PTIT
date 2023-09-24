class ThiSinh:
    __cnt = 1
    def __init__(self, ten, diem, danToc, khuVuc):
        self.__ma = "TS" + "0" * (2 - len(str(ThiSinh.__cnt))) + str(ThiSinh.__cnt)
        self.__diem = diem
        self.__danToc = danToc
        self.__khuVuc = khuVuc

        tach = ten.split()
        self.__ten = ""
        for x in tach: self.__ten += x.title() + " "

        if danToc != "Kinh": self.__diem += 1.5
        if khuVuc == 1: self.__diem += 1.5
        elif khuVuc == 2: self.__diem += 1

        if self.__diem >= 20.5: self.__trangThai = "Do"
        else: self.__trangThai = "Truot"

        ThiSinh.__cnt += 1

    def __str__(self):
        return self.__ma + " " + self.__ten + ("%.1f" % self.__diem) + " " + self.__trangThai

    def getDiem(self):
        return self.__diem
    
    def getMa(self):
        return self.__ma

res = []
for _ in range(int(input())):
    res.append(ThiSinh(input(), float(input()), input(), int(input())))

res.sort(key = lambda x: x.getDiem(), reverse = True)

for x in res: print(x)