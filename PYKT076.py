from datetime import datetime

class TheLoai:
    __cnt = 1
    def __init__(self, tenTheLoai):
        self.__maTheLoai = "TL{:03d}".format(TheLoai.__cnt)
        TheLoai.__cnt += 1
        self.__tenTheLoai = tenTheLoai
    
    def get_maTheLoai(self):
        return self.__maTheLoai
    
    def get_tenTheLoai(self):
        return self.__tenTheLoai

class Phim:
    __cnt = 1
    def __init__(self, maTheLoai, ngayKhoiChieu, tenPhim, soTapPhim, theLoai):
        self.__maPhim = "P{:03d}".format(Phim.__cnt)
        Phim.__cnt += 1
        self.__maTheLoai = maTheLoai
        self.__ngayKhoiChieu = ngayKhoiChieu
        self.__tenPhim = tenPhim
        self.__soTapPhim = soTapPhim
        self.__objTheLoai = theLoai
    
    def __lt__(self, other):
        if self.__ngayKhoiChieu == other.__ngayKhoiChieu:
            if self.__tenPhim == other.__tenPhim:
                return self.__soTapPhim > other.__soTapPhim
            return self.__tenPhim < other.__tenPhim
        return datetime.strptime(self.__ngayKhoiChieu, r"%d/%m/%Y") < datetime.strptime(other.__ngayKhoiChieu, r"%d/%m/%Y")

    def __str__(self):
        return self.__maPhim + " " + self.__objTheLoai.get_tenTheLoai() + " " \
    + self.__ngayKhoiChieu + " " + self.__tenPhim + " " + self.__soTapPhim

n, m = map(int, input().split())
listTL = []
for i in range(n):
    listTL.append(TheLoai(input()))

listPhim = []
for i in range(m):
    maTL, objTL = input(), None
    for j in listTL:
        if j.get_maTheLoai() == maTL: 
            objTL = j
            break
    listPhim.append(Phim(maTL, input(), input(), input(), objTL))

listPhim.sort()
print(*listPhim, sep = '\n')