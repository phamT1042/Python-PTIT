from datetime import datetime

class MonThi:
    def __init__(self, maMonThi, tenMonThi):
        self.__maMonThi = maMonThi
        self.__tenMonThi = tenMonThi
    
    def get_maMonThi(self):
        return self.__maMonThi
    
    def get_tenMonThi(self):
        return self.__tenMonThi

class CaThi:
    __cnt = 1
    def __init__(self, maMonThi, ngayThi, gioThi, nhomThi, MonThi):
        self.__maCaThi = "T{:03d}".format(CaThi.__cnt)
        CaThi.__cnt += 1
        self.__maMonThi = maMonThi
        self.__ngayThi = ngayThi
        self.__gioThi = gioThi
        self.__nhomThi = nhomThi
        self.__objMonThi = MonThi
    
    def __lt__(self, other):
        if self.__ngayThi == other.__ngayThi:
            if self.__gioThi == other.__gioThi:
                return self.__maMonThi < other.__maMonThi
            return self.__gioThi < other.__gioThi
        return datetime.strptime(self.__ngayThi, r"%d/%m/%Y") < datetime.strptime(other.__ngayThi, r"%d/%m/%Y")

    def __str__(self):
        return self.__maCaThi + " " + self.__objMonThi.get_maMonThi() + " " + \
    self.__objMonThi.get_tenMonThi() + " " + self.__ngayThi + " " + self.__gioThi + " " + self.__nhomThi

n, m = map(int, input().split())
listMonThi = []
for i in range(n):
    listMonThi.append(MonThi(input(), input()))

listCaThi = []
for i in range(m):
    data, objMonThi = input().split(' '), None
    for j in listMonThi:
        if j.get_maMonThi() == data[0]: 
            objMonThi = j
            break
    listCaThi.append(CaThi(data[0], data[1], data[2], data[3], objMonThi))

listCaThi.sort()
print(*listCaThi, sep = '\n')