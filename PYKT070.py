class MonThi:
    def __init__(self, maMon, tenMon, hinhThucThi):
        self.__maMon = maMon
        self.__tenMon = tenMon
        self.__hinhThucThi = hinhThucThi
    
    def get_maMon(self):
        return self.__maMon

    def get_tenMon(self):
        return self.__tenMon
    
    def __str__(self):
        return self.__maMon + " " + self.__tenMon + " " + self.__hinhThucThi
    
class CaThi:
    __cnt = 1
    def __init__(self, ngayThi, gioThi, phongThi):
        self.__maCaThi = "C{:03d}".format(CaThi.__cnt)
        CaThi.__cnt += 1
        self.__ngayThi = ngayThi
        self.__gioThi = gioThi
        self.__phongThi = phongThi
    
    def get_maCaThi(self):
        return self.__maCaThi

    def get_ngayThi(self):
        return self.__ngayThi

    def get_gioThi(self):
        return self.__gioThi

    def get_phongThi(self):
        return self.__phongThi

    def __str__(self):
        return self.__maCaThi + " " + self.__ngayThi + " " + self.__gioThi + " " + self.__phongThi

class LichThi:
    def __init__(self, maCaThi, maMon, maNhom, soSinhVien, objMonThi, objCaThi):
        self.__maCaThi = maCaThi
        self.__maMon = maMon
        self.__maNhom = maNhom
        self.__soSinhVien = soSinhVien

        self.__objMonThi = objMonThi
        self.__objCaThi = objCaThi 
    
    def __lt__(self, other):
        if self.__objCaThi.get_ngayThi() == other.__objCaThi.get_ngayThi():
            if self.__objCaThi.get_gioThi() == other.__objCaThi.get_gioThi():
                return self.__maCaThi < other.__maCaThi
            return self.__objCaThi.get_gioThi() < other.__objCaThi.get_gioThi()
        return self.__objCaThi.get_ngayThi() < other.__objCaThi.get_ngayThi()

    def __str__(self):
        return self.__objCaThi.get_ngayThi() + " " + self.__objCaThi.get_gioThi() + " " + \
    self.__objCaThi.get_phongThi() + " " + self.__objMonThi.get_tenMon() + " " + self.__maNhom + " " + self.__soSinhVien

input = open("MONTHI.in", "r")
n = int(input.readline())
listMonThi = []
for i in range(n):
    listMonThi.append(MonThi(input.readline().rstrip('\n'), input.readline().rstrip('\n'), input.readline().rstrip('\n')))
input.close()

input = open("CATHI.in", "r")
m = int(input.readline())
listCaThi = []
for i in range(m):
    listCaThi.append(CaThi(input.readline().rstrip('\n'), input.readline().rstrip('\n'), input.readline().rstrip('\n')))
input.close()

input = open("LICHTHI.in", "r")
k = int(input.readline())
listLichThi = []
for i in range(k):
    thongTin = input.readline().rstrip('\n').split(' ')
    saveCaThi, saveMonThi = None, None
    for j in listCaThi:
        if thongTin[0] == j.get_maCaThi(): 
            saveCaThi = j
            break
    for j in listMonThi:
        if thongTin[1] == j.get_maMon():
            saveMonThi = j
            break
    listLichThi.append(LichThi(thongTin[0], thongTin[1], thongTin[2], thongTin[3], saveMonThi, saveCaThi))
input.close()

listLichThi.sort()
print(*listLichThi, sep = '\n')

