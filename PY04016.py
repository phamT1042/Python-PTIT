from datetime import datetime

class KhachSan:
    __cnt = 1
    def __init__(self, ten, soPhong, ngayNhan, ngayTra, phiDV):
        self.__ma = 'KH{:02d}'.format(KhachSan.__cnt)
        KhachSan.__cnt += 1
        self.__ten = ten
        self.__soPhong = soPhong
        self.__ngayNhan = ngayNhan
        self.__ngayTra = ngayTra
        self.__phiDV = phiDV

        self.__soNgay = (datetime.strptime(self.__ngayTra, "%d/%m/%Y") - datetime.strptime(self.__ngayNhan, "%d/%m/%Y")).days + 1

        if self.__soPhong[0] == '1':
            self.__tien = 25 * self.__soNgay
        elif self.__soPhong[0] == '2':
            self.__tien = 34 * self.__soNgay
        elif self.__soPhong[0] == '3':
            self.__tien = 50 * self.__soNgay
        else:
            self.__tien = 80 * self.__soNgay
        
        self.__tien += self.__phiDV

    def __str__(self):
        return self.__ma + " " + self.__ten + " " + self.__soPhong + " " + str(self.__soNgay) + " " + str(self.__tien)

    def __lt__(self, other):
        return self.__tien > other.__tien
    
n = int(input())
listKH = []
for _ in range(n):
    listKH.append(KhachSan(input().strip(), input().strip(), input().strip(), input().strip(), int(input())))

listKH.sort()
print(*listKH, sep = '\n')

